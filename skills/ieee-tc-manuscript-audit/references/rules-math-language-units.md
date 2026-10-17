# Rules extracted from manual pages 24–45

This is a source-derived reference fragment for `ieee-tc-manuscript-audit`, not a separate IEEE TC submission specification. Page numbers below mean both the physical PDF page and the printed page number in this supplied edition. The complete text of pages 24–45 was read. Page images 27, 28, 36, 38, 39, and 44 were also inspected to resolve spelling, star-marker, exponent, and table-column ambiguities. These rules use only the supplied manual, including its explicit exceptions and internal inconsistencies.

## Contents

- [Classification and scope](#classification-and-scope)
- [Mathematics and references](#mathematics-and-references)
- [Layout](#layout)
- [Grammar, punctuation, and hyphenation](#grammar-punctuation-and-hyphenation)
- [Acronyms and units](#acronyms-and-units-prevent-false-positives)
- [Dictionary lookup](#routing-to-the-source-instead-of-duplicating-dictionaries)
- [Unsupported conclusions](#explicitly-unsupported-conclusions-from-pages-2445)
- [Reading record](#reading-and-verification-record)

## Classification and scope

- **明确要求**: an explicit imperative, prohibition, or mandatory wording in the manual; this alone does not make it an IEEE TC submission requirement.
- **推荐做法**: an explicit `should`, `preferably`, `preferred`, or similar recommendation. Normally report nonconformity as `RECOMMENDED_IMPROVEMENT` rather than a mandatory violation.
- **一般建议**: a usage guide or lookup aid that needs context and human judgment.
- `CONFIRMED_VIOLATION` requires an unambiguous source rule, applicability, and manuscript evidence. No text-search hit alone qualifies.
- Technical meaning, ambiguous wording, conflicting source entries, or a needed data/unit interpretation → `AUTHOR_CONFIRMATION_REQUIRED`.
- General layout statements describe IEEE edited/typeset presentation. Do not claim that a float position establishes rejection at submission, or apply a two-column production rule to an unverified single-column review format.
- Do not change the manuscript during the audit. Hyphenation, punctuation, capitalization, and unit fixes can affect meaning; only propose minimal changes and flag their risks.

## Mathematics and references

### M-MATH-01 — Referring to equations

- Source: p. 24, item 14. Short evidence: “Use the word ‘Equation’ at the start of a sentence” and “in text, just use the number”.
- Force/scope: **明确要求**, general IEEE editorial style for prose references.
- Rule: Begin a sentence with `Equation (n)`; within a sentence refer to `(n)` rather than introducing a different equation label format.
- Method: Inspect prose around every equation reference in source and rendered PDF; distinguish the equation label itself from prose mentioning an equation concept.
- Decision: An unambiguous mismatching reference form can be `CONFIRMED_VIOLATION`; a correctly formatted checked reference is `PASS`.
- Exceptions/risks: Do not replace a mathematical expression with an equation reference or change numbering. Preserve legitimate text that discusses equations without citing one.

### M-MATH-02 — Variables, operators, units, and descriptive subscripts

- Source: p. 24, “Displayed Equations”. Short evidence: “All variables are italic”; “Function names and abbreviations are Roman”.
- Force/scope: **明确要求**, mathematical typography, not a prescription of a particular LaTeX package.
- Rule: Variables are italic; named functions, units/unit abbreviations, complete words, and word abbreviations are roman. Apply the same distinction to superscripts and subscripts.
- Method: Pair source math with the PDF; identify the role of each symbol before checking upright/italic appearance. Inspect e.g. textual `in`/`out` subscripts, function operators, and unit tokens.
- Decision: Clear role plus wrong typography → `CONFIRMED_VIOLATION`; unclear variable-versus-label role → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception: The manual permits single-letter superscripts/subscripts to be italic even when abbreviations, unless that creates inconsistent treatment of similar subscripts. Do not flag every single-letter subscript.

### M-MATH-03 — Equation punctuation and lead-ins

- Source: p. 24, “Use of Periods and Commas”. Short evidence: “Equations which conclude a sentence should end with a period.”
- Force/scope: **推荐做法** for sentence-final periods; the same paragraph gives explicit editorial instructions on lead-ins and terminal commas.
- Rule: Treat an equation as part of its sentence. Punctuation before a displayed equation is used when the lead-in is a complete sentence. End-of-equation commas are removed unless critical to the sentence's punctuation.
- Method: Read the full sentence spanning the display, not just its last TeX line. Check a rendered equation and its adjacent prose.
- Decision: Missing terminal period → normally `RECOMMENDED_IMPROVEMENT`; a clear conflicting explicit punctuation instruction can support `CONFIRMED_VIOLATION`. Ambiguous grammatical attachment → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception: Critical sentence commas are expressly retained. Do not indiscriminately remove commas or add colons before every display.

### M-MATH-04 — Equation numbering and placement

- Source: p. 24, “Equation Numbers”. Short evidence: “should be consecutive” and “should not have repeats or missing numbers”.
- Force/scope: **推荐做法**, equation presentation.
- Rule: Consecutive numbering, no repeated/missing numbers, number flush right and aligned with the last line of the equation, using a correct numbering style.
- Method: Compare rendered numbers in reading order with labels/references and `.aux`/build diagnostics where available. Determine whether multipart numbering is deliberate.
- Decision: Report style deviations as `RECOMMENDED_IMPROVEMENT`; unresolved or incorrect references are separate engineering findings, not proof of an IEEE submission violation. Explain an ambiguous numbering scheme with `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception: The excerpt does not define every legal appendix/subequation numbering scheme. Do not infer that parenthesized letter suffixes or appendix prefixes are forbidden.

### M-MATH-05 — Ellipses and conditions after displays

- Source: p. 24, “Ellipses” and “Conditions”. Short evidence: “When commas are used, the ellipses are on the baseline.”
- Force/scope: **明确要求**, equation typography; context-sensitive.
- Rule: In a sequence with comma separators, use baseline dots; for operational signs, center the dots on the operators. Retain appropriate separators after terms and after the dots. Consult the rendered source for condition spacing and the exception before the for-all symbol.
- Method: Inspect the rendered equation, not plain extracted text; lost math glyphs and spaces in extraction are not evidence of a defect.
- Decision: Clear typography mismatch → `CONFIRMED_VIOLATION`; uncertain operator role/condition grouping → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception/source caution: Some examples in the extracted text become visually indistinguishable. Do not construct automated replacements from flattened examples. This rule cannot authorize rewriting a formula.

### M-UNIT-01 — Compound units

- Source: p. 24, “Compound Units”. Short evidence: “Compound units should be separated by a center dot”.
- Force/scope: **推荐做法**.
- Rule: Separate multiplied units with a centered dot; a slash and a negative exponent may express a denominator. Parentheses may clarify grouping.
- Method: Review numeric values and units in prose, tables, axes, and math; first establish multiplication versus division.
- Decision: Typographic improvement → `RECOMMENDED_IMPROVEMENT`; ambiguity that could change the measured dimension → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception: Slash and negative-power forms are explicitly permitted. Never change `V/s` into `V·s`, since the manual expressly notes their different meanings.

## Layout

### M-LAYOUT-01 — Figure/table placement and reading order

- Source: pp. 24–25, “F. General Layout Rules”, items 1–2. Short evidence: “at the tops of columns as close to their first mention as possible” and “progress vertically, not horizontally”.
- Force/scope: Column-top/vertical ordering is a general **明确要求** in the edited-layout section; placing after first mention is explicitly **推荐做法** (“preferably”). Applicability to the submission variant must be established separately.
- Rule: In the applicable column layout, place figures/tables near first mention, generally at column tops, and arrange their reading progression vertically.
- Method: Inspect the rendered PDF with first mentions marked. Check actual positions and reading order rather than interpreting `[t]`, `[h]`, or source order as proof.
- Decision: For a manuscript not verified to use that production layout, report a layout observation as `RECOMMENDED_IMPROVEMENT` or `AUTHOR_CONFIRMATION_REQUIRED`, not a journal submission rejection rule. For an explicitly audited matching typeset layout, a clear source conflict may be `CONFIRMED_VIOLATION`.
- Exception: “as close ... as possible” and “preferably” allow judgment. A float appearing before its first mention is not, by that fact alone, a confirmed mandatory violation.

### M-LAYOUT-02 — Footnote column

- Source: p. 25, item 3. Short evidence: “Footnotes must appear at the bottom of the column where they are first mentioned.”
- Force/scope: **明确要求**, column-layout production rule.
- Method: Inspect each rendered footnote marker and the location of its footnote text; account for any special first-page footnote treatment established elsewhere in the manual.
- Decision: If the applicable column layout and footnote type are established, a different column supports `CONFIRMED_VIOLATION`; otherwise report `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception: Do not infer review-template requirements or force manual placement commands solely from this production rule.

## Grammar, punctuation, and hyphenation

### M-GRAM-01 — Serial comma

- Source: p. 26, “A. Rules of Grammar”, item 2. Short evidence: “In a series of three or more terms, use a comma immediately before the coordinating conjunction”.
- Force/scope: **明确要求**, running prose.
- Method: Read candidate lists in context and establish at least three coordinated terms. Do not count internal conjunctions or mathematical operators as prose list members.
- Decision: An unmistakable list missing the serial comma → `CONFIRMED_VIOLATION`; complex grammatical grouping → `AUTHOR_CONFIRMATION_REQUIRED`.
- Risk: Punctuation can change grouping and therefore meaning. Propose only the exact comma insertion after validating the intended grouping.

### M-GRAM-02 — Parenthetic elements and restrictive clauses

- Source: p. 26, item 3. Short evidence: “never omit one comma and leave the other”; “‘that’ is preferred”.
- Force/scope: Balanced parenthetic punctuation and nonrestrictive clause commas are **明确要求**; preference for `that` in restrictive clauses is **推荐做法**.
- Rule: Parenthetic insertions take paired commas when commas are used. Nonrestrictive clauses use `which` with surrounding commas. The paragraph explicitly permits restrictive `that` or `which`, preferring `that`.
- Method: Parse the complete sentence and determine restrictive/nonrestrictive meaning before judging punctuation or pronouns.
- Decision: A missing half of an unmistakable paired insertion → `CONFIRMED_VIOLATION`; restrictive `which` alone → at most `RECOMMENDED_IMPROVEMENT`, never automatically a violation; ambiguous restriction → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exceptions: The manual permits omission of both commas for a slight interruption. Do not impose a comma after every occurrence of `however` or replace every `which` with `that`.

### M-GRAM-03 — Clauses, colons, and semicolons

- Source: p. 26, items 4–5. Short evidence: “Use a colon after an independent clause to introduce a list.”
- Force/scope: **明确要求** for the colon context; general usage guidance for semicolons joining independent clauses, including conjunctive adverbs.
- Method: Identify clause boundaries in the full sentence. Inspect list introductions and conjunctive adverbs such as `however` and `therefore`.
- Decision: A clear colon-after-fragment issue under the stated list rule can be `CONFIRMED_VIOLATION`; stylistic choice among valid joins → `RECOMMENDED_IMPROVEMENT`; uncertain grammar → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception: Do not apply prose list punctuation to equation notation or code. Do not require a semicolon where another grammatically valid sentence structure exists.

### M-GRAM-04 — Quotes and nested parentheses

- Source: p. 26, items 6–8. Short evidence: “Direct quotes should be set in quotation marks in roman font”; “Do not use double parentheses in text expressions”.
- Force/scope: The explicit prohibitions/instructions are **明确要求**; direct-quote roman phrasing uses **推荐做法** (“should”).
- Rule: Follow the manual's quotation-mark punctuation convention, with colon and semicolon outside; use single marks for quotes within quotes. Avoid italicizing direct quotes. In text, replace nested round parentheses with an outer square pair (its example is `[see (10)]`).
- Method: Check full quotations and their punctuation in source and PDF. Distinguish direct quotation from emphasis, mathematical notation, and literal software strings.
- Decision: Clear instruction mismatch → `CONFIRMED_VIOLATION`; roman-font preference → `RECOMMENDED_IMPROVEMENT`; literal/technical syntax at risk → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exceptions: Nested parentheses in mathematics are expressly retained. Do not change quoted technical text or executable/literal syntax to satisfy a general prose convention.

### M-GRAM-05 — Apostrophes, plurals, and possessives

- Source: p. 26, items 1 and 9. Short evidence: “All acronyms and numerical plurals do not use apostrophes”.
- Force/scope: **明确要求**, prose grammar.
- Rule: Acronym and numeral plurals normally lack apostrophes (manual examples: `FETs`, `1980s`). Distinguish plural from possessive and possessive pronouns from contractions.
- Method: Read each candidate apostrophe in context; determine whether it denotes a plural, ownership, or contraction.
- Decision: Confirmed plural-only apostrophe → `CONFIRMED_VIOLATION`; ambiguous ownership or mathematical convention → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception: The manual notes mathematical-writing exceptions. Never transform a genuine possessive such as `VM's state` into a plural.

### M-GRAM-06 — Context-dependent hyphenation

- Source: pp. 26–27, items 10–16; spelling/hyphenation lookup pp. 32–35. Short evidence: “Do not hyphenate predicate adjectives”; “A hyphen is not used after the comparative or the superlative”.
- Force/scope: Stated prohibitions and grammatical rules are **明确要求**; “generally” and dictionary lookup are **一般建议**.
- Rule: Distinguish attributive compounds from predicate adjectives, adjective pairs modifying a noun independently, `-ly` adverbs, comparative/superlative forms, compound verbs, and their derived nouns. Use the supplied pp. 32–35 list as a lookup, retaining its part-of-speech labels.
- Method: Inspect each occurrence's grammatical role and the exact manual entry before suggesting a change. Examples relevant to computing include `bandwidth` (p. 32), `database` (p. 32), `lookup table` (p. 33), `higher order` (p. 33), `throughput` (p. 34), and `worst case (adj)` (p. 35).
- Decision: Clear context and unambiguous rule conflict → `CONFIRMED_VIOLATION`; preference/general usage → `RECOMMENDED_IMPROVEMENT`; ambiguous technical compound or source conflict → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exceptions/source caution: Page 27's verbal hyphen rule conflicts with some of its displayed spellings (`highfrequency`, `secondorder`, `freezedried`, `arcwelded`), confirmed in the PDF image. Do not copy these as prescriptive replacement strings. Do not globally hyphenate every compound adjective or globally normalize named techniques, identifiers, products, titles, or code. The manual's external dictionary suggestion is not authorization to add another normative source in this PDF-only skill.

### M-GRAM-07 — Word-choice and spelling lookup

- Source: p. 27, “Words Often Confused”, and pp. 32–35, “Common Hyphenations and Misspellings”. Short evidence: “Fewer: modifies plural nouns specifying countable units”.
- Force/scope: **一般建议**, semantic usage and lookup.
- Method: Use the exact relevant entry only when needed, reading the entire sentence; do not replicate all dictionary entries in the skill. Examples include `affect/effect`, `fewer/less`, `imply/infer`, and `principal/principle`.
- Decision: A possible wrong word ordinarily merits `RECOMMENDED_IMPROVEMENT` or `AUTHOR_CONFIRMATION_REQUIRED`; a clear listed orthographic spelling can support `CONFIRMED_VIOLATION` only when it is unambiguous ordinary prose, not a proper name or literal.
- Exception/source caution: A usage list does not authorize technical rewriting. Internal inconsistencies or apparent source mistakes must be reported, not silently repaired by outside knowledge.

## Acronyms and units: prevent false positives

### M-ABBR-01 — Appendix A definition exemptions

- Source: p. 28 note and pp. 28–31 entries. Short evidence: “Other terms listed here may be used without definition.”
- Force/scope: **明确要求** for starred terms; explicit permission for the unstarred terms in this appendix and their listed meanings.
- Rule: Asterisked terms require a definition at first use in text. Unstarred listed terms can be used without a definition. Consult all applicable entries, not a blanket “every acronym must be defined” pattern.
- Method: Build an acronym occurrence inventory, distinguish abstract/body scopes using the manual's relevant general rule, then look up the exact abbreviation and intended meaning. Manually review possible exemptions before reporting.
- Useful checked entries: `CPU` has no asterisk (p. 28); `DMA` has an asterisk (p. 29); `FTP`, `GUI`, `HTML`, `I/O`, and `LAN` have none (p. 29); `PC` has none (p. 30); `RAM`, `ROM`, and `QoS` have none, while `SOC` and `VLSI` have asterisks (p. 31).
- Decision: Correctly scoped first-use omission for an unambiguous starred/nonexempt term may be `CONFIRMED_VIOLATION`. Undefined `CPU` in its listed meaning must not be labeled a confirmed violation solely for lacking expansion. An unlisted abbreviation is not automatically exempt; consult the general rule elsewhere in this manual.
- Exceptions: Meaning matters (`SI` has both an unstarred and a starred meaning on p. 31). The tables include semantic and spelling irregularities; do not automatically overwrite the manuscript's expansion from the table.

### M-ABBR-02 — Conflicting abbreviation entries

- Source: p. 28, `ATM`, and pp. 43–44, Appendix D key and `ATM` entry. Short evidence: p. 43 says “*—acronyms that must be defined in text.”
- Force/scope: A **source limitation**, not a new normative rule.
- Observed conflict: `ATM` / asynchronous transfer mode is unstarred on p. 28 but starred on p. 44; visually confirmed in both page images. `av` also differs in star treatment between p. 28 and p. 44.
- Method: When checking any disputed abbreviation, show both source locations and the manuscript occurrence. Do not choose the stricter rule merely to maximize findings.
- Decision: `AUTHOR_CONFIRMATION_REQUIRED` with reason `SOURCE_INTERNAL_CONFLICT`; optionally recommend expansion for readability without claiming a confirmed IEEE violation.
- Exception: This conflict does not invalidate every unambiguous exemption elsewhere. Keep narrow, evidence-based treatment.

### M-UNIT-02 — Unit table columns and symbol case

- Source: pp. 35–43, “C. Table of Units and Quantity Symbols”; p. 35 header. Short evidence: “Sometimes Occur as: (do not use)”.
- Force/scope: **明确要求** for explicit excluded unit symbols; the notes separately identify preferences and deprecations.
- Rule: Distinguish unit symbol, disallowed variant, quantity variable, and explanatory notes. Asterisks here designate SI/acceptable-with-SI units, not “must define” (the asterisk convention differs from the acronym appendix).
- Method: Inspect the actual table columns in the PDF for any candidate rule. Check symbol case, prefix, and meaning in the manuscript. Do not infer a unit from a capital letter without context.
- Decision: A clearly applicable explicitly excluded symbol supports `CONFIRMED_VIOLATION`; a merely deprecated or nonpreferred unit normally supports `RECOMMENDED_IMPROVEMENT`; unknown physical meaning → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exceptions: Proper names, literal hardware specifications, data-column labels copied from tools, and code need context. Do not convert measured values or units during a read-only audit. Do not import the contents of ANSI/IEEE/ISO sources cited by the table.

### M-UNIT-03 — Bits, bytes, and rates

- Source: p. 36 entries `bit`, `bit per second`, `byte`; p. 39 `kilobit per second`; p. 40 `megabit per second`; p. 45 `bps`. Short evidence: p. 45: “bit per second: use b/s”.
- Force/scope: Unit symbol mappings and explicit `use` instruction are **明确要求**, given an established intended measurement.
- Rule: The table maps bit to `b`, byte to `B`, and bit per second to `b/s`; the corresponding rate entries include `kb/s` and `Mb/s`. Do not treat uppercase and lowercase `B/b` as interchangeable.
- Method: Compare all prose/table/axis rate labels with the experiment's documented meaning. Establish whether a measure is bit throughput or byte throughput before diagnosing case.
- Decision: Obvious symbol style conflict with known measurement → `CONFIRMED_VIOLATION`; no evidence of intended bit/byte meaning → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception: The manual is not evidence of what the author's benchmark actually measures. Never silently multiply/divide data by eight or replace `MB/s` with `Mb/s`.

### M-UNIT-04 — Decimal versus binary prefixes

- Source: p. 38 (`gibi`, `giga`, `gigabyte`, `kibi`); p. 39 (`kilo`, `kilobyte`, `mebi`, `mega`); p. 40 (`megabyte`); p. 42 (`tebi`, `tera`, `terabyte`). Short evidence: p. 39: “The prefix kilo shall not be used to mean” 2^10; “The prefix mega shall not be used to mean” 2^20.
- Force/scope: **明确要求** for the explicit binary/decimal prohibitions and the table definitions. Superscripts were verified visually on pp. 38–39.
- Rule: The source defines Ki = 2^10, Mi = 2^20, Gi = 2^30; decimal kilo = 10^3, mega = 10^6, giga = 10^9. It gives kB = 1000 bytes (p. 39), MB = 1,000,000 bytes (p. 40), GB = 10^9 B (p. 38), and Ti = 2^40 / T = 10^12 (p. 42). These are meanings, not evidence of what any reported value represents.
- Method: Audit labels against documented base and exact magnitude. Distinguish intended quantity, nominal product capacity, and literal command/output text. If changing the prefix would change represented size, require author confirmation.
- Decision: A manuscript explicitly equating kilo with 1024 or mega with 2^20 conflicts with the manual and can be `CONFIRMED_VIOLATION`; an unexplained `MB` memory size is not sufficient to prove that conflict → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception/source conflict: The p. 39 kilo row simultaneously lists unit symbol `k` and says “The symbol k shall not be used for kilo.” This contradiction is visible in the page image, not merely an extraction error. Do not generate a blanket prohibition on `k`, silently change the quote to `K`, or resolve it using outside standards. Mark a decision depending on that sentence `AUTHOR_CONFIRMATION_REQUIRED` / `SOURCE_INTERNAL_CONFLICT`. The separate decimal/binary definitions remain usable.

### M-UNIT-05 — Temperature and roman unit/function typography

- Source: p. 37 (`degree Fahrenheit` notes), p. 38 (`kelvin`), p. 43 Appendix D key. Short evidence: p. 37: “no space between the ° and the letter that follows”; p. 43: “fn—function name (roman); s—symbol (italic); u—unit abbreviation (roman)”.
- Force/scope: **明确要求**, symbolic presentation; applicable only to the identified symbol type.
- Rule: Keep the two parts of °C/°F/°R together; kelvin uses `K` without a degree sign. Appendix D's function, variable, and unit annotations determine roman/italic presentation.
- Method: Inspect PDF glyphs, superscripts, and spacing alongside source math. Do not confuse spacing inside `°C` with spacing between a numerical value and the full unit, whose applicable rule must be checked separately.
- Decision: A clear mismatch for the established unit/function → `CONFIRMED_VIOLATION`; an uncertain symbol identity → `AUTHOR_CONFIRMATION_REQUIRED`.
- Exception: A token can represent different things (e.g. unit, variable, acronym, or identifier). The source table cannot determine its role in an arbitrary formula without context.

## Routing to the source instead of duplicating dictionaries

- Abbreviation exemptions and starred definitions: Appendix A, pp. 28–31.
- Hyphenations and common spellings: Appendix B, pp. 32–35. Respect `(adj)`/`(noun)` annotations; do not use a whole-document find/replace.
- Unit symbols, explicitly excluded variants, prefixes, preferred/deprecated units: Appendix C, pp. 35–43. Always consult the PDF image where column alignment or exponents are ambiguous.
- Mixed abbreviation/function/symbol lookup begins at Appendix D, p. 43, continues beyond this fragment. Its key is on p. 43. Only pages 43–45 of that appendix are represented here; the full skill must use the remaining manual pages before claiming complete dictionary coverage.
- Source mentions external dictionaries and standards, but this skill's normative scope stays with the provided PDF. Their full requirements are `NOT_COVERED_BY_SOURCE` unless the user separately authorizes and supplies them.

## Explicitly unsupported conclusions from pages 24–45

These pages do not establish IEEE TC page limits, anonymous-review policy, submission-system rules, an exact `IEEEtran` option set, a required TeX engine, a prohibited package list, a PDF page-size dimension, acceptable overfull-box thresholds, font embedding requirements, or automatic acceptance/rejection criteria. Do not invent them. If an engineering check is performed, label its findings as technical evidence and use the full supplied manual to determine whether a normative claim is actually supported.

## Reading and verification record

- Complete text read: PDF/printed pp. 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45.
- Page images inspected: 27, 28, 36, 38, 39, 44.
- Source caveats retained: p. 27 hyphenation examples; p. 28 versus p. 44 `ATM` star conflict; p. 39 kilo-symbol contradiction; table exponents/column roles must not be inferred from flattened extraction.
- No external normative material used; no manuscript files changed.
