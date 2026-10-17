# 手册后段规则摘记（PDF 第 46–67 页）

## 阅读与来源记录

- 已完整逐页读取 `pages-46-67.txt` 中 PDF 物理页 46–67（印刷页相同），另读取第 43 页词典图例以解释星号与字体标记。第 44 页亦已读。
- 已以 Poppler 渲染并实际查看第 56、57、61、62、63、64、65、66、67 页；核实了概率符号、单位幂以及四列表格中术语、替换词、背景说明及脚注的归属。
- 原始手册在创建过程中变更了本机存放位置。随技能保存的 `source-manual.pdf` 为 67 页、809723 字节，所查页与提取文本吻合；重新执行 `pdftotext -layout` 后，完整提取文本与最初源 PDF 的提取文本逐字节相同。
- 本段只支持字典、符号、单位缩写、部分数学写法及包容语言的编辑审计。它不提供 IEEE TC 当前页限、匿名政策、投稿系统、指定编译器/文档类选项或完整参考文献细则。

## 可纳入规则库的条目

“手册力度”是对原文的区分；它与报告状态不是同一维度。只有适用语境已确认且原文明确要求时才可判 `CONFIRMED_VIOLATION`。表格检索命中本身不是违规。

| ID | 规则与范围 | 手册页码与短原文 | 手册力度 | 检查方法与判定限制 |
|---|---|---|---|---|
| DICT-01 | 词典字体图例：函数名正体，符号斜体，单位缩写正体 | p.43: `fn—function name (roman); s—symbol (italic); u—unit abbreviation (roman)` | 明确词典约定 | 先核对该词在论文中的实际含义，再检查源码及成品字形；字母相同但含义不同不应替换。需要确认语义则 `AUTHOR_CONFIRMATION_REQUIRED`。 |
| DICT-02 | 词典带星号的缩写必须在正文定义 | p.43: `*—acronyms that must be defined in text.` | 明确要求 | 对匹配缩写查首次出现与定义。不可反推未标星号的所有条目都豁免定义；还须应用正文缩略语规则。 |
| DICT-03 | 缩写、大小写和含义须按上下文查词典 | pp.46–61；如 p.47 `dc ... (DC at start of sentence or in article title)` | 词条约定 | 避免将一种学科含义强行套到另一种含义。例如同页 `DC` 也列为 directional coupler；p.49 `GPU` 有多义，p.46 `CNN` 是该词典的特定定义，不得据此重写论文的技术定义。 |
| DICT-04 | 单位词条给出的替代缩写可作为编辑依据 | p.51 `kbps (u) ... use kb/s`；p.58 `sec ... (u) second: use s`；p.57 `rpm ... use r/min` | 明确词条用法 | 必须区分单位与函数/名称，如 `sec` 作为 secant 不改成 `s`；代码标识符、引用原题目及产品名不能机械替换。注意只调整表示，不换算或改变数值。 |
| DICT-05 | `psi` 的替换有明确例外 | p.56: `change to lb/in2 unless paper also contains psia and/or psig` | 明确且有条件 | 全文检查是否出现 psia/psig，再判 `psi`。`psia` 和 `psig` 词条都标 `stet`，应保留。PDF 上的 2 是上标，提取文本不反映字形。 |
| DICT-06 | 数学词条中 `use` 也须先确认含义 | p.57: `Re ... be sure of this meaning before changing`；p.59 `tg ... use tan` | 明确且语境依赖 | 查式子中是否确指实部、正切；同名变量或不同数学定义不自动改。p.56 概率符号项含 `use Pr (usually)`，属于通常做法而非无条件命令。 |
| DICT-07 | 十进制单位前缀的大小写与倍率 | p.61 表头 `Factor by Which the Unit Is Modified / Prefix / Symbol`；如 kilo k、mega M、milli m、micro μ | 明确查表值 | 只对单位前缀用途核对。表内为十进制倍率；不能把 KB/MB 的语义仅靠大小写推断为二进制或改动实验数据。p.61 对二进制前缀只是指向 NIST 表 7；若需外部细节，在唯一 PDF 来源模式下标 `NOT_COVERED_BY_SOURCE`，不得假装已查 NIST。 |
| INCL-01 | 包容语言总则为 people-first，按具体语境处理 | p.61 `Overall recommendations:`；`Use “people-first language,”` | 明示推荐 | 默认 `RECOMMENDED_IMPROVEMENT`；不把人的相关术语匹配强加给计算机技术词，例如 invalid memory address、normal distribution。 |
| INCL-02 | 特定常见缩写不展开；保留语境限定 | p.61: `Do not spell out the acronyms LGBTQIA+, LGBT, LGBTQ, LGBTQIA.`；p.65 LGBT 条件 `If needed for clarity` | 总体推荐中的明确指示，另有情境例外 | 一般不得把这些缩写未展开判为违规。p.65 的受众条件可能支持展开；需要受众判断时 `AUTHOR_CONFIRMATION_REQUIRED`，不制造绝对禁令。 |
| INCL-03 | 技术替代词是表中优选词，不能默认等价或强制 | p.62 Black box → Closed box；Blacklist → Blocklist；p.65 Master/Slave → leader/follower、parent/child、primary/secondary、main/secondary；p.67 White box → Glass box、Whitelist → Access list；表注 `Preferred term from IEEE Thesaurus` | 明确为优选，非 TC 专用要求 | 默认 `RECOMMENDED_IMPROVEMENT`；先确认技术语义、引用名称、接口名是否变化。尤其不用全局查找替换改代码、标准名称或贡献描述。 |
| INCL-04 | 关于人群的替代词取决于实际指代 | p.62 African American 注 `not to be used as an umbrella`；p.64 Indian 条目只针对 Indigenous People，且印度原住民/居民义可用 | 有上下文限制的建议 | 不根据出现单词就报错；地域、族群和当事人称谓不明则 `AUTHOR_CONFIRMATION_REQUIRED`。 |
| INCL-05 | 直接引文、临床语境的明确例外应保留 | p.63 某些精神健康词条 `Except in a quote or when referring to a criminal defense.`；p.64 Dwarf `Use only when applied to a medical diagnosis or in a quote.`；p.64 Invalid（名词）`Except when used in a direct quote` | 明确条件及豁免 | 必须读对应整行和脚注。不能把一个词条的引文例外自动扩张成全表通用例外。不要自行给人添加诊断，也不要修改引用原文。 |
| INCL-06 | Deaf 的大小写取决于身份/偏好，词性亦有说明 | p.63: `Capitalize for those who identify as members of the Deaf community` | 情境性编辑建议 | 不能统一转小写；身份或偏好未给出时请求作者确认。 |
| INCL-07 | 诊断替换有事实前提 | p.66 Learning disability 注 `Only when the condition has been medically diagnosed` | 明确条件 | 不能为替换一个词而凭空断言医学诊断；缺证据时 `AUTHOR_CONFIRMATION_REQUIRED`。 |
| INCL-08 | 人名及代词遵循本人身份信息 | p.66: `Always use a transgender person’s chosen name.` | 明确要求，适用事实需确认 | 仅在已提供当事人的名字/代词信息且论文明显违背时才能判断。不得猜测身份、名字或代词。 |
| INCL-09 | unmanned → autonomous 属优选建议，存在潜在语义变化 | pp.66–67，相关车辆词条注 `Preferred term from IEEE Thesaurus` | 推荐 | 不能把遥控系统改写成自主系统。先报告最小替代建议及语义风险，含义不同则请作者确认。 |

## 字典的按需使用方法

1. 只提取论文实际使用的词条，记录词条页码、符号/单位/缩写角色、全文语境和首次出现处；不复制整份词典进 `SKILL.md`。
2. 检查候选项时读取该行完整上下文及表头图例。p.46–61 是 p.43 开始的词典延续，不是独立缩略语定义豁免清单。
3. 先确认词义，再判字形、大小写、连字符或推荐替代。技术定义不一致、同一缩写有多义、原文疑似错误时保留稿件并报告 `AUTHOR_CONFIRMATION_REQUIRED`。
4. 提取文本会丢上标或把符号排布拉平。涉及单位幂、概率符号、上下标、斜体/正体时回看 PDF 页面；不得把提取文本直接当最终排版样例。
5. Appendix 的链接不代表链接文献已作为规范读过；只有本 PDF 内实际写出的内容属于这次的规范来源。

## 已核查的源文歧义，防止生成虚假违规

- p.62 的 Blind 行在 Definition/Background 中为 `20/200`，Additional Notes 中为 `20/2000`，渲染图确认两个值确实不同。不要擅自选择其一当审计门槛；遇此用途标作者确认和源文歧义，不作医学判断。
- p.61 的一般缩写建议与 p.65 的特定受众场景应同时记录，不把前者覆盖后者。
- p.63 Cripple 与 p.64 Deformed/deformity 的替换文字带 `*`，但该行未见对应脚注说明；不要编造该星号代表的例外。
- p.66 的 autonomous 替代只属词表优选，不能确认所有 unmanned 技术场景都与自主控制等价。
- 不用词典给出的一个展开强行替换稿件中明确、有效的另一种技术含义；这属于内容修改而非无风险格式修正。

## 覆盖限制

本段没有提供参考文献作者名顺序、DOI 的完整语法、卷期/页码模板或 TC 当前投稿政策。其他页若只给外部 Reference Guide 链接，也不能在本次唯一 PDF 来源模式下补入未读外部规范。工程质量（编译成功、missing glyph、嵌入字体、页面尺寸、overfull）应与 IEEE 规范依据分开记录；不能从本段词表推导 LaTeX 宏包/编译器禁令。
