#!/usr/bin/env python3
"""Read-only technical diagnostics; never classifies IEEE compliance."""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


def run_tool(name, arguments):
    exe = shutil.which(name)
    if not exe:
        return {"state": "UNAVAILABLE", "reason": f"{name} not on PATH"}
    try:
        result = subprocess.run([exe, *arguments], capture_output=True, text=True,
                                encoding="utf-8", errors="replace", timeout=60)
        return {"state": "OK" if result.returncode == 0 else "ERROR",
                "command": [exe, *arguments], "exit_code": result.returncode,
                "stdout": result.stdout, "stderr": result.stderr}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"state": "ERROR", "reason": str(exc)}


def log_records(text):
    """Join wrapped LaTeX warning lines, retaining the first physical line number."""
    lines = text.splitlines()
    warning = re.compile(r"^(?:LaTeX(?: Font)? Warning:|Package \S+ Warning:)")
    new_message = re.compile(r"^(?:LaTeX|Package \S+|!|Overfull|Underfull|Missing character:|No file |I can't find file|Output written on|.+?:\d+:\s)")
    index = 0
    while index < len(lines):
        start = index + 1
        parts = [lines[index]]
        index += 1
        if warning.match(parts[0]):
            while index < len(lines) and lines[index].strip() and not new_message.match(lines[index]):
                parts.append(lines[index].strip())
                index += 1
        yield start, " ".join(parts)


def collect(pdf, log):
    evidence = {"basis": "TECHNICAL_DIAGNOSTIC", "ieee_compliance": "NOT_DETERMINED",
                "pdf": str(pdf), "log": str(log) if log else None,
                "limitations": ["Log and PDF pairing must be established separately.",
                                "Message counts are not independent defect counts.",
                                "No build executed; no exit code or visual layout verified."]}
    info = run_tool("pdfinfo", [str(pdf)])
    evidence["pdfinfo"] = info
    count = re.search(r"^Pages:\s+(\d+)", info.get("stdout", ""), re.MULTILINE)
    if count:
        evidence["pdfinfo_all_pages"] = run_tool("pdfinfo", ["-f", "1", "-l", count[1], str(pdf)])
    fonts = run_tool("pdffonts", [str(pdf)])
    evidence["pdffonts"] = fonts
    rows = []
    for line in fonts.get("stdout", "").splitlines():
        # The last five fields are emb/sub/uni/object ID/generation; font type can contain spaces.
        match = re.match(r"^(.*?)\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+(\d+)\s+(\d+)\s*$", line)
        if match:
            rows.append({"font_description": match[1], "embedded": match[2] == "yes",
                         "subset": match[3] == "yes", "unicode_map": match[4] == "yes"})
    evidence["font_rows"] = rows
    evidence["all_listed_fonts_embedded"] = all(r["embedded"] for r in rows) if rows and fonts["state"] == "OK" else None
    if log:
        text = log.read_text(encoding="utf-8", errors="replace")
        patterns = {
            "undefined_citation_messages": r"Citation .+ undefined",
            "undefined_reference_messages": r"Reference .+ undefined",
            "undefined_summary_messages": r"There were undefined (?:references|citations)",
            "missing_character_messages": r"Missing character:",
            "missing_file_messages": r"(?:File .+ not found|I can't find file|No file .+)",
            "overfull_messages": r"Overfull \\[hv]box",
            "underfull_messages": r"Underfull \\[hv]box",
            "font_warning_messages": r"(?:LaTeX Font Warning:|Some font shapes were not available|Size substitutions)",
            "fatal_messages": r"(?:^!|Fatal error|Emergency stop)",
        }
        records = list(log_records(text))
        evidence["log_messages"] = {key: [{"line": i, "text": line}
            for i, line in records if re.search(pattern, line)]
            for key, pattern in patterns.items()}
        evidence["message_counts"] = {k: len(v) for k, v in evidence["log_messages"].items()}
        evidence["log_output_written"] = bool(re.search(r"Output written on", text))
        evidence["log_engine_header"] = text.splitlines()[0] if text else ""
    return evidence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--log", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    pdf = args.pdf.resolve()
    log = args.log.resolve() if args.log else None
    for item in [pdf, log]:
        if item is not None and not item.is_file():
            parser.error(f"Input file not found: {item}")
    out = args.out.resolve()
    destination = out / "build-evidence.json"
    if destination in [pdf, log]:
        parser.error("Output must not overwrite an input")
    evidence = collect(pdf, log)
    out.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    print(destination)


if __name__ == "__main__":
    main()
