# IEEE 论文审计 Skills

## ieee-tc-manuscript-audit

依据随附的 **IEEE Editorial Style Manual for Authors（Updated 29 July 2024，67页）**，对 IEEE/IEEE TC 论文进行只读编辑规范与 LaTeX/PDF 工程审计。

- [技能入口](skills/ieee-tc-manuscript-audit/SKILL.md)
- [规则索引](skills/ieee-tc-manuscript-audit/references/style-rules.md)
- [检查清单](skills/ieee-tc-manuscript-audit/references/checklist.md)
- [规范来源与限制](skills/ieee-tc-manuscript-audit/references/source-notes.md)

检查范围包括标题、摘要、关键词、缩写、标点与连字符、图表引用、数字与单位、手册涉及的参考文献规则，以及编译、交叉引用、字体嵌入和版面诊断。报告保留手册页码、论文页码、源码行号和最小修改建议，并区分确认违规、建议、作者确认、来源未覆盖及通过。

## 安装与使用

将仓库内 `skills/ieee-tc-manuscript-audit` 整个文件夹复制到个人 Codex 技能目录（通常为 `~/.codex/skills/`；自定义环境使用 `$CODEX_HOME/skills/`），保留其中的 `references`、`scripts` 和 `agents`。

在加载该技能的新聊天中使用：

```text
使用 $ieee-tc-manuscript-audit 对以下论文进行只读审计。
PDF：<当前论文PDF路径>
主源码：<与PDF匹配的主TeX路径>
输出 MANUSCRIPT_AUDIT.md 和 AUDIT_COVERAGE.md，不修改论文。
```

可选工程证据脚本需要 Python 3，以及 PATH 中的 `pdfinfo`、`pdffonts`；它本身不编译论文。编译检查使用论文已有工具链，并在副本中执行。

## 边界

唯一规范来源是随附手册。本技能不代表已核实 IEEE TC 当前页数限制、匿名政策、投稿系统或专用模板要求，也不把编译成功等同于完整格式合规。默认不修改稿件；修复仅针对明确批准的修改清单。

此仓库仅包含技能和配套手册，不包含用于本地试运行的论文、实验数据或构建产物。
