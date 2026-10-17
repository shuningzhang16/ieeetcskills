# LaTeX/PDF 工程检查：与规范结论分开

这些检查用于发现实际技术问题。除非能指出本PDF具体条款，不把工程故障升级为IEEE/TC违规。指定编译器、文档类选项、字体嵌入、页面尺寸和告警阈值未在本手册建立。

## 隔离与构建

1. 读主TeX、includes、bibliography、类文件/构建说明，辨别项目实际引擎；不要自动替换类、字体、宏包或迁移引擎。
2. 复制必要工程文件到新输出目录，例如 `audit/build/`。输入文件原样保留。涉及绝对/父目录依赖时先明确依赖，不能悄悄引用另一个版本。
3. 在副本中调用明确的工具，不执行未知Makefile/脚本，不启用shell-escape。普通pdfLaTeX/BibTeX项目可依次运行：

   ```text
   pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
   bibtex main
   pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
   pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
   ```

   仅有实际BibTeX依赖时运行bibtex；biber/其他引擎按现有项目处理并说明。工具缺失只记录，不自动更换论文工程。保存每步退出码和控制台日志。遇首个实质错误停止并报告，不在只读审计中修稿。
4. 检查最终.log/.blg/.bbl以及新生成PDF。首轮交叉引用尚未解析的警告不能当最终失败；BibTeX产生重复key或缺条目必须逐项核实。编译退出码为0且真实生成PDF才可报告构建成功。
5. `pdffonts`检查实际各字体嵌入状态；另查LaTeX字体形状缺失和替换警告，嵌入成功不能证明未发生字体替换。`pdfinfo -f 1 -l N`检查各页尺寸/旋转/页数。工具失败或只看第一页时不能宣布全PDF通过。字体允许名单与页面合规阈值未覆盖。
6. 渲染并查看各页，重点查图表、边界、标题、参考文献和日志定位区域。Overfull要结合实际溢出，Underfull往往只是松散排版；两者均非自动IEEE违规。图像内缺字/错轴标签也可能不出现在TeX日志。

## 可选证据收集器

`scripts/collect_build_evidence.py`只读取PDF/日志并调用系统的pdfinfo/pdffonts，写诊断文件；不编译、不修改稿件、不判IEEE规范：

```text
python scripts/collect_build_evidence.py --pdf /absolute/build/main.pdf --log /absolute/build/main.log --out /absolute/audit/evidence
```

脚本用Python标准库；pdfinfo/pdffonts缺失时写明不可用。可以用等价工具手动获取，但报告应写明实际方法。换行的LaTeX警告合并为一条消息，并保留起始日志行号；日志命中数量不等于独立缺陷数。脚本无法证明PDF与日志同一构建，也不能证明命令退出码或视觉布局，且错误列表并不穷尽所有TeX错误格式；审计者必须另行核对。

## 工程结果分类

- 实际检查正常：PASS，依据标`TECHNICAL_DIAGNOSTIC`，手册页码“不适用”，不代表IEEE合规。
- 技术错误但手册没有对应规范：NOT_COVERED_BY_SOURCE，同时记录`technical_result=FAIL`、严重程度和可复现证据，不能隐藏故障。
- 警告只有建议意义：RECOMMENDED_IMPROVEMENT，依据标工程观察，明确不是手册强制规定。
- 缺工具/缺源码/未构建：覆盖表NOT_TESTED，不能报PASS；有关完整规范的发现列NOT_COVERED_BY_SOURCE。

源代码行号来自实际文件；PDF页码从实际新PDF定位，必要时使用synctex或文本定位并视觉复核。不确定时写“未定位”，不把TeX输出页号、日志输入行号或手册页码混为一谈。
