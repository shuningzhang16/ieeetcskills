# 报告结构

报告使用用户语言，保留英文原文。先交代审计对象、阶段/假设、唯一规范来源版本、PDF页数、与源码是否对应、是否做了新构建、是否改动原稿。声明IEEE TC专用投稿层未核实。

## MANUSCRIPT_AUDIT.md

1. 摘要：五种类别各自数量、关键故障、未验证事项。不能将建议数量算入确认违规。
2. 具体发现：每项采用下列字段（无适用字段不能略去，写原因）。

```text
ID: A001
Category: 五类之一
Severity: HIGH / MEDIUM / LOW / INFO
Check state: CHECKED / NOT_TESTED / NOT_APPLICABLE
Basis: SOURCE_RULE / TECHNICAL_DIAGNOSTIC / USER_REQUIREMENT / SOURCE_GAP
Manuscript: PDF物理页与可见章节/图表/文献号
Source location: 绝对路径或工程相对路径 + 实际行号；无源码写未提供
Current text: 逐字原文/渲染内容；提取断词与原文区别说明
Rule: 规则ID、source-manual.pdf实际页、短摘录、明确/推荐/建议力度
Applicability: 文章类型、阶段、上下文、已排除的例外
Evidence/method: 实际查看、计数、图像核对或命令与结果
Minimal suggestion: 最小候选修改或待确认问题；PASS可写无需修改
Impact: 语义、实验数据/精度、页面布局分别说明
Unverified: 未验证项目、定位局限、外部信息缺失
```

严重程度与类别独立：HIGH用于实际阻碍阅读/编译或重大歧义，MEDIUM为实质格式问题，LOW为局部编辑，INFO为通过/覆盖说明。HIGH并不意味着IEEE拒稿。

3. 工程证据：引擎、命令/退出码、新PDF路径、未定义引文/交叉引用、missing file/figure/character、字体、页尺寸、Overfull/Underfull。区分“0条日志消息”与“独立问题数为0”。
4. 未覆盖：TC页限/费用/匿名/投稿系统/模板版本，以及本手册未提供的完整参考文献样式和工程规格。
5. 修复清单：若用户请求修复，逐ID列原文、精确新文、风险、是否已批准。未经明确批准不实施；已批准项目不重复请求。

PDF页与源码无法对应时，分别列页码和源码候选位置，标注未确认映射。不要为了填字段编造精确行号或未见原文。分组PASS可以共用一条记录，但必须列具体检查范围、方法、适用规则和证据；不可声称未读完整内容的全文PASS。

## AUDIT_COVERAGE.md

逐行覆盖checklist.md全部主题，列检查范围、进度、类别/发现ID、输入证据、剩余缺项。对抽样说明样本页和不能外推的范围。将SOURCE_GAP与工具不足区分：前者没有规范依据，后者没能检查；两者不能互相掩盖。
