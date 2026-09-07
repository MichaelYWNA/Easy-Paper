# Easy-Paper Prompt Examples

## Project Intake

```text
$easy-paper 接入 D:\Your\Paper\Project。先扫描 main.tex、references.bib、章节结构、引用键、图片、交叉引用和编译命令，不要修改正文。
```

## Literature First

```text
$easy-paper 围绕我的题目检索 2020-2026 年的高质量论文，优先找综述、方法论文和与我的研究场景相近的应用论文。输出候选文献表、检索记录和 evidence-map，不要直接写正文。
```

## Reference-Informed Introduction Revision

```text
$easy-paper 读取我提供的 15 篇参考论文和我的 main.tex。请先建立 reference-style-map 和 evidence-map，再逐段修改 Introduction。每句话都要说明：原句问题、证据来源、参考论文的写作动作、原创改写、上下文逻辑检查和风险。
```

## Section Diagnosis Only

```text
$easy-paper 只诊断 Methodology，不写回 main.tex。请输出逐段逐句 revision-ledger，指出哪些句子缺少证据、哪些句子过度声称、哪些地方 LaTeX 或术语可能有风险。
```

## Compile-Safe Patch

```text
$easy-paper 修改 Results and discussion 的指定段落，保持所有公式、图表、label、cite key 不变。修改后检查 citation/bib 同步和 LaTeX 编译风险。
```

## Full Paper Revision

```text
$easy-paper 对整篇 LaTeX 论文做 evidence-led revision。先生成任务包和章节蓝图，然后按章节逐段处理。每章完成后更新 evidence-coverage、logic-review 和 easy-paper-progress。
```
