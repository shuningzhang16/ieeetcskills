---
name: ieee-tc-manuscript-audit
description: "依据随附 IEEE Editorial Style Manual，只读审计 IEEE/IEEE TC 论文的编辑规范、图表、缩写、数字、参考文献及 LaTeX/PDF 工程质量，提供可追溯的手册页码与最小修改建议。用于论文格式审查或投稿前检查；不自动改写论文，不宣称覆盖尚未核实的 IEEE TC 专用投稿要求。"
---

# IEEE 论文编辑与 LaTeX 审计

## 来源与边界

唯一规范来源为 [source-manual.pdf](references/source-manual.pdf)：IEEE Editorial Style Manual for Authors，封面标注 Updated 29 July 2024，共 67 页。它是一般 IEEE 编辑手册，不是当前 IEEE TC 投稿指南。不要联网补充规范、以惯例补写规则，或把论文、源码注释和历史报告当成规范。

页码使用从 1 开始的 **PDF 物理页**；正文印刷页与物理页相同，封面无印刷页。目录部分页码滞后一页，不能直接引用。详见 [来源说明](references/source-notes.md)。

默认只读。报告和隔离构建产物可以写入新输出目录；不得覆盖原 main.pdf、源码、BibTeX、图片或实验数据。不为本技能新增 hash、冻结 contract、baseline 或 gate。

## 执行流程

1. **确认输入。** 记录 PDF、主 TeX、包含文件、图片、书目和日志的路径与版本依据。用户指定的最新稿优先，不能因文件名为 main.tex 就选择旧稿。判断 PDF 与源码是否对应；无法确认就分开审计，不伪造逐页映射。缺源码仍可审 PDF，缺项记入未验证表。
2. **识别阶段。** 区分投稿稿、返修稿、出版校样；未知则说明假设。匿名、出版日期、DOI、版权、通讯作者、ORCID、传记等涉及阶段或事实，先列 AUTHOR_CONFIRMATION_REQUIRED，不把出版样式变成投稿门槛。
3. **建立证据。** 提取 PDF 分页文本；数学、表格、字形、大小写、间距、引用和断词有疑义时渲染并查看完整相关页。按实际包含顺序读取源码。查 [规则索引](references/style-rules.md) 及相关分支，再查源 PDF 对应页面；短摘录只是定位锚点，不能省略同段例外。
4. **逐项审计。** 用 [checklist.md](references/checklist.md) 记录覆盖。正则、词频、缩写扫描和字数统计只生成候选，不能自动判违规。PDF 提取造成的换行连字、双栏顺序、符号丢失不是原文错误。摘要和正文分别查缩写，考虑 Nomenclature 与第28–31页明确豁免；不机械改产品名、引用标题、算法代码或技术标识符。
5. **检查工程。** 按 [latex-quality.md](references/latex-quality.md) 在工程副本中构建，检查最终日志、实际 PDF、字体和版面。不要在原工程运行会覆盖 PDF 的编译；不要为消警告执行未知脚本或启用 shell-escape。工具不可用时继续静态审计并列缺项；已有日志只能证明历史构建。
6. **形成报告。** 按 [report-format.md](references/report-format.md) 输出报告和覆盖表。每项确认违规都有明确规则、适用条件和论文直接证据。PDF 页码或源码行号无法确定时写“未定位”及原因。PASS 只代表列明规则在已检查范围内通过。

## 判定纪律

每项发现仅用以下一个类别，严重程度另列：

| 类别 | 使用条件 |
|---|---|
| CONFIRMED_VIOLATION | PDF 明确要求，适用阶段/语境已确认，论文直接违反，例外已排除。 |
| RECOMMENDED_IMPROVEMENT | 来源为 generally / preferred / encouraged 等建议，或说明清楚的编辑建议；不得包装成强制要求。 |
| AUTHOR_CONFIRMATION_REQUIRED | 需核实作者事实、技术含义、有效数字、授权、投稿阶段，或来源内部冲突。 |
| NOT_COVERED_BY_SOURCE | PDF 未建立所需规范，尤其 TC 专用要求和工程标准；仍可报告测量和技术错误。 |
| PASS | 实际检查通过，列依据、范围与方法；技术检查注明“工程结果，非 IEEE 合规结论”。 |

进度单独记 `CHECKED`、`NOT_TESTED`、`NOT_APPLICABLE`。未检查不等于 PASS；无相应内容记不适用，不凭抽样宣布全文通过。

强度按所引用的具体句子判断：仅由should / should always / generally / preferred支持的项目默认是建议；同一段中的must、shall、直接禁止或明确处方另行判断。不能因表格行混合了不同力度，就将整行都升格为确认违规。

## 内容保护与修复

- 不改实验数值、单位含义、有效数字、技术主张、贡献或结论；不为页数删除句子。
- 建议保留原文与最小候选修改，说明语义、数据和版面影响。存在多种合理解释时请作者确认。
- 授权修复时先生成具体清单，只实施明确批准项目。会话中已有明确批准持续有效，不重复确认；笼统修复不能扩大为未列明的技术改写。
- 修复后复查受影响规则、重新构建和查相应页面；不能修改手册让论文通过。

## 交付

生成 `MANUSCRIPT_AUDIT.md` 与 `AUDIT_COVERAGE.md`，工程证据放同目录 `evidence/`。最终给实际路径、各类发现数量、关键未验证项和是否改动论文。不得宣称“IEEE TC 全面合规”“保证录用”或“编译通过所以格式合格”。
