# 规则索引与证据

页码均为source-manual.pdf实际PDF页。短摘录用于定位，必须检查原段例外。强度“明确”是编辑处方；不等于适用所有投稿阶段。

按主题读：[数学/语法/单位](rules-math-language-units.md)（24–45页）；[术语/包容语言](rules-terminology-inclusive.md)（46–67页）；[来源局限](source-notes.md)；[工程诊断](latex-quality.md)。

## 结构、摘要与作者

| ID | 页/强度 | 短原文锚点 | 检查与判定边界 |
|---|---|---|---|
| S01 | 4/明确 | “unnecessary changes” | 不改技术原意；意义不明待作者确认。 |
| S02 | 5/推荐 | “should generally be written in the following order” | 检查标题、摘要、关键词、引言、正文、结论、附录、致谢、参考文献顺序；不强制Design等章节，不创造缺章。 |
| S03 | 5,10/明确 | “one paragraph and between 150 to 250 words” | 摘要一段150–250词；报告计数方法，断词/公式/复合词临界值人工复核。 |
| S04 | 10/明确 | “nor footnotes” | 摘要无编号公式、编号引文和脚注；不能禁止所有行内数学。 |
| S05 | 10/明确 | “All articles must contain Index Terms” | 关键词存在、按字母顺序、首词大写，其余按专名语境；缩写全称在前括号在后。未规定数量上限。 |
| S06 | 5/明确/推荐分开 | “Prepositions of more than three letters” | 首句should支持的词类大小写默认建议；同段长于3字母介词及首末词的直接大小写规定分别核查，保留单位等例外。详细公式只是discouraged。 |
| S07 | 5–6,15/条件 | “Use the same information in both places” | 作者姓名、会员级别在byline/传记一致；不补造姓名或会员事实。 |
| S08 | 6/条件 | “required for the corresponding author” | 通讯作者ORCID属作者/系统确认事项；PDF未印不代表未提交，不能伪称查过TC投稿系统。 |
| S09 | 6–9/条件 | “country and corresponding author’s e-mail address MUST be included” | 根据阶段核对单位、国家、通讯邮箱、占位符；匿名或未知作者信息先确认，不造日期/邮箱/DOI。 |
| S10 | 7,13/明确有例外 | “All financial support” | 资助通常放首脚注，有刊物和OA指定措辞例外；没资助段不证明有遗漏。 |
| S11 | 9–10/条件 | “https://doi.org/theFullDOI” | 有补充材料/在线彩色图时核对对应出版脚注；投稿未分配DOI不违规。 |
| S12 | 11/混合 | “desirable, but not required” | 章节编号可选；已有编号对照四级格式。References/Acknowledgment不编号，Acknowledgment单数无多余e；生产字形按阶段说明。 |
| S13 | 12/明确 | “Do not use the word ‘Subsection’” | 正文交叉引用用Section II/II-A，Section大写；不能偷偷改合法模板编号体系。 |
| S14 | 11–12/明确有例外 | “leave the Appendix unnumbered” | 单附录不编号；多附录I/A均可；附录图表与正文连续。附录公式(A1)允许。 |
| S15 | 12–13/条件 | “shall be disclosed” | AI生成内容及范围由作者确认；仅编辑/语法增强的披露是recommended。不能因用审计技能就认定必需披露。 |
| S16 | 12–13/明确有例外 | “Write the Acknowledgment section in the third person” | 有致谢时检查位置/第三人称，Editorial有18页例外，保留特殊资助措辞。 |
| S17 | 15–16,19/条件 | “If all authors ... opt not” | 核查实际提供的传记/照片；短文和全体不提供有例外，缺传记不能直接判投稿违规。 |

## 引用与图表

| ID | 页/强度 | 短原文锚点 | 检查与判定边界 |
|---|---|---|---|
| R01 | 13/明确 | “one reference per number” | 每书目编号一项来源；同时看.bbl和PDF。 |
| R02 | 13/明确 | “do not belong on the reference list” | 不把For example等独立说明塞书目；标题里的原词不能删。 |
| R03 | 13–14/明确有例外 | “in [1]” | 不用in reference [1]；作者名为句意主体/日期与主题相关时允许保留。 |
| R04 | 14/明确 | “in [1, Fig. 2]” | 来源内图、式、节等按[1, Fig. 2]/[1, eq. (8)]定位，区别本稿图号。 |
| R05 | 14/推荐 | “should all be made into one reference” | 建议将同源不同页重复列号合并；版本、论文/代码是否同源须核实，不能仅凭相似标题去重，也不把should-only直接判违规。 |
| R06 | 14/明确 | “check its spelling against the reference list” | 文中作者名与书目拼写一致；不能据此验证原始书目信息真实性。 |
| R07 | 13–14/未覆盖 | 少量书目示例 | 未完整规定各类型标题大小写、姓名缩写、卷期页码、DOI标点。可查字段丢失、转义/特殊字符和一致性；其完整规范判NOT_COVERED_BY_SOURCE，不新增论文/DOI。 |
| F01 | 14/明确 | “All first citations ... in numerical order” | 按真实正文阅读顺序分别核对图/表首次引用，后续回引允许；排除外部[1, Fig.2]和图注标签。 |
| F02 | 14/明确 | “always carry the abbreviation ‘Fig.’” | 图引用用Fig.，句首亦然；同图(a)(b)仍单数；检查宏渲染，不凭源码推断最终空格。 |
| F03 | 14/推荐 | “should always be capitalized” | 图号后句点、首词大写、图注脚注位置均按原段should表述作为建议；不以A/An/The开头也是in general建议。 |
| F04 | 14–15/明确/推荐分开 | “several acceptable styles” | 全稿一致是直接指示，分图(a)(b)在对应说明前由should always支持，默认建议；不要强改所有合法形式。跨页图按具体原句核对Continued。 |
| F05 | 15/明确/推荐分开 | “label TABLE ... Roman numerals” | 表题上方、TABLE罗马编号及居中是general style/should建议；描述末尾无句点为直接规定，内部可有标点。倒金字塔为一般建议。 |
| F06 | 14/明确 | “will no longer accept ... ‘Lena image’” | 图像确认出现才列，不凭文件名猜测。 |
| F07 | 15/条件 | “obtaining in advance permission” | 复用图核来源引文与授权；缺授权文件先问作者，不推断侵权。 |

## 编辑、数字与数学

| ID | 页/强度 | 短原文锚点 | 检查与判定边界 |
|---|---|---|---|
| E01 | 17–18/语境 | “grammatically parallel” | 分别检查run-in、完整句、不完整句和where列表；脚注按序且在对应列底部，首脚注另有例外。 |
| E02 | 21,28–31/明确有例外 | “in the Abstract as well as ... body” | 摘要/正文分别首次定义，Nomenclature后正文可不重复；必须查Appendix A豁免，例如CPU，不把所有大写串都当缩写。 |
| E03 | 21/明确 | “do not take the apostrophe” | 复数FETs，不用FET’s；所有格不同，冠词按发音。 |
| E04 | 21/明确 | “Change all British spellings to American” | 仅作者普通行文；真标题、姓名、机构、引文、代码保留。本PDF外词典未读取，不能称查过最新词典。 |
| E05 | 21–22/明确/语境 | “hyphenation ... is consistent” | 比较相同语法角色；定语/表语可不同；用26–27规则及32–35查表。意义不明先确认。 |
| E06 | 22/明确 | “the word ‘to’ must be used” | 范围用en dash，from配to；排除负号和代码减号。 |
| E07 | 22/明确 | “The data were collected” | data复数、a series单数、主谓和平行；多义或抽取不清先确认。 |
| E08 | 22/明确有例外 | “are not used in technical text” | don’t/can’t普通口语展开；don’t care等专门术语例外保留。 |
| E09 | 22/推荐 | “In general, discourage capitalization” | 非必要大写只建议；Guest/Native等可能实验组定义，先核实。 |
| N01 | 23/明确 | “does not include references” | 正文日期日-完整月名-年；不套用参考文献日期。 |
| N02 | 23/明确 | “symbol is repeated in lists and ranges” | 百分比数值+%，列表/范围各项重复%；百分比与百分点含义不能改。 |
| N03 | 23/语境冲突 | “if needed for clarity” / “Always add a zero” | 文本与数学前导零分开，尾零关系精度时作者确认；见source-notes。 |
| N04 | 23/推荐 | “there should be no unit after each number” | 同单位范围建议40–50 mm，异单位各自保留；百分比有明确重复规则，不能混用。 |
| N05 | 23–24/明确/推荐分开 | “Variables are set italic” | 变量斜体，向量usually粗斜体为推荐；函数、单位正体按角色和渲染核查。 |
| N06 | 23/明确 | “regular space and not a thin space” | 正文数值与单位普通空格；无数值单位拼全称；先区分数学、表头、角度/百分号，不全局替换薄空格。 |
| N07 | 23/明确 | “62 000, 100 000, but 4000” | 手册明确说明数万/数十万用薄空格而非逗号，并给4000不分组的例子；不要把例子扩大成所有数字的无条件规则。排除年份、ID、版本、代码、引文定位。 |
| N08 | 23/明确有例外 | “spell out numbers below 11” | 带单位数字，其他小于11拼写，句首/组合范围有例外；统计参数/标识语义不明时确认。 |
| N09 | 23/明确 | “Use zeroth, first, nth” | 正文序数；保留真实会议名称、原题目与变量语境。 |
| N10 | 12/明确有例外 | “numbered consecutively” | 一般公式连续，部分刊物允许分节，附录(A1)允许；未知刊物规则不自动判其非法。 |

第18–20页的Editorial、Brief、Letters、Comments/Replies、Corrections及Book Reviews仅对相应文章类型适用；不套入普通研究论文。
