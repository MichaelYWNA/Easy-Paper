---
name: easy-paper
description: Use when revising or drafting academic papers in LaTeX with verified literature evidence, paragraph-by-paragraph and sentence-level commentary, citation mapping, logic checks, and compile-safe edits. Do not use for plagiarism, patchwriting, or bypassing academic integrity.
metadata:
  short-description: "Evidence-guided LaTeX paper revision"
  version: "0.1.0"
  created: "2026-09-07"
---

# Easy-Paper

Easy-Paper 是一个面向 LaTeX 论文的证据驱动修订 skill。它的目标不是把别人的论文逐句换皮，而是把参考论文转化为可核验的写作范式、论证结构、证据地图和引用位置，然后逐段、逐句修订用户自己的 `.tex` 稿件。

## 使用边界

- 可以学习参考论文的章节功能、论证顺序、证据类型、结果呈现方式、谨慎措辞和连接逻辑。
- 可以短摘录参考论文中的少量句子用于分析写法，但最终稿必须使用原创表达，并标注相应证据来源。
- 不得复制、拼接、近似改写或“降重”参考论文的连续表达。
- 不得把参考论文的研究对象、数据、实验条件、公式、结论或引用移入用户论文，除非这些内容本来就是用户研究的一部分且已被独立核验。
- 引用必须可追溯。无法验证的文献、无法确认支持关系的引用、以及只靠模型记忆生成的参考文献不能进入最终稿。

## 何时使用

当用户要求以下任务时使用本 skill：

- 修改、润色、重写、扩写、定稿 LaTeX 论文。
- 根据 10-15 篇参考论文帮助重构自己的论文。
- 检索高质量文献并将其转化为 evidence map、文献综述、引言、讨论或投稿稿件。
- 对 `main.tex`、`references.bib`、`plan/` 中的论文项目做逐段评论、逐句修订、引用检查、逻辑审稿或编译验证。

若任务只是普通问答、非学术写作、或用户明确要求学术不端式洗稿，说明边界后改用合规方案。

## 第一步

每次使用 Easy-Paper 时，先判断当前任务属于哪一类，并只读取对应参考文件：

| 任务 | 必读参考 |
|---|---|
| 初次接入一个论文项目或模板 | `references/latex-project-intake.md` |
| 检索、筛选、补充文献 | `references/literature-retrieval.md` |
| 根据参考论文修订正文 | `references/evidence-led-revision.md` |
| 使用用户的 Elsevier CAS 海洋工程模板 | `references/latex-cas-template.md` |
| 修改 Easy-Paper 自身 | `references/extension-points.md` |

如果任务跨多个类别，按“项目接入 -> 文献检索 -> 证据地图 -> 逐段修订 -> 验证”的顺序读取。

## 项目工作区

默认在论文项目根目录内维护以下文件：

```text
paper-project/
|-- main.tex
|-- references.bib
|-- figures/
|-- tables/
|-- chapters/
`-- plan/
    |-- project-overview.md
    |-- easy-paper-progress.md
    |-- evidence-map.md
    |-- reference-style-map.md
    |-- revision-ledger.md
    |-- chapter-blueprints/
    |-- task-packets/
    `-- review/
        |-- evidence-coverage.md
        |-- citation-verification.md
        |-- logic-review.md
        `-- latex-build.md
```

`main.tex` 是默认唯一主稿。除非用户的项目明确使用拆分章节，所有最终修订都回到 LaTeX 文件中完成。

## 核心流程

1. **接入 LaTeX 项目**：定位主 `.tex`、BibTeX 文件、模板类型、章节层级、引用命令、图表路径和编译命令。优先运行 `scripts/latex_project_inspect.py`。
2. **建立文献池**：优先使用用户提供的 PDF、BibTeX、DOI、CNKI 导出、Zotero/EndNote 记录或笔记；用户要求检索时，再使用 OpenAlex、Crossref、Semantic Scholar、PubMed/arXiv/Europe PMC 等来源。
3. **建立证据地图**：每条来源必须对应可写入正文的具体 supported claim、citation slot、证据强度和风险，不接受“这篇很相关”式空泛记录。
4. **建立参考风格地图**：记录参考论文的结构动作，例如“先定义问题边界，再比较方法族，再给研究缺口”，不记录可复用原句。
5. **逐段读取原文**：先读取目标章节的完整上下文，再拆成段落和句子。可运行 `scripts/latex_revision_sheet.py` 生成 `plan/revision-ledger.md` 骨架。
6. **逐句修订**：每句话都要给出问题判断、可用证据、引用位置、原创改写、上下文逻辑检查和剩余风险。没有证据的强判断要降级或标记为待补证据。
7. **写回 LaTeX**：保留模板命令、公式、图表、标签、交叉引用、引用键和 BibTeX 风格。修改时优先小范围补丁。
8. **验证**：完成前至少检查 evidence coverage、citation/bib 同步、逻辑连续性和 LaTeX 编译状态。能编译就编译；不能编译要说明缺少的工具或文件。

## 与四个 GitHub 项目的融合方式

Easy-Paper 吸收四个上游项目的可复用思想，详见 `references/upstream-integration.md`：

- `dsebastien/ai-skill-scholar`：OpenAlex 检索、引用量筛选、两轮文献综述会话。
- `K-Dense-AI/scientific-agent-skills` 的 `paper-lookup`：多数据库检索选择、API 失败模式、provenance 记录。
- `federicodeponte/opendraft`：research -> structure -> compose -> QA -> export 的多阶段流水线，以及 citation existence 与 claim support 分离。
- `Imbad0202/academic-research-skills`：深度研究、证据等级、反方审查、伦理与学术诚信门控。

这些项目作为工作流参考，不作为允许复制外文句子的授权。

## LaTeX 安全规则

- 优先保留用户模板和现有 `.tex` 结构；不要把正文改成 Markdown。
- 对 Elsevier CAS 模板，使用 `\section`、`\subsection`、`\subsubsection`，保持 `natbib` 的 `\citep`/`\citet` 风格和 `cas-model2-names`。
- 不要随意新增宏包、改变 `\documentclass`、重命名图片、重排长表、删除 `\label` 或改动公式。
- 新增引用必须同步更新 `references.bib`，并在 `plan/review/citation-verification.md` 记录 DOI、检索来源和确认状态。
- 每次修订后检查是否破坏 `\ref`、`\cite`、数学环境、浮动体和特殊字符转义。

## 输出格式

对用户汇报时保持简洁，但论文项目内必须留下可审计文件。一次正文修订至少产出或更新：

- `plan/revision-ledger.md`：逐段逐句修订账本。
- `plan/evidence-map.md`：证据到论点映射。
- `plan/easy-paper-progress.md`：本轮任务、输入、输出、验证和剩余风险。
- 修改后的 `.tex` 文件；若只做诊断，则明确没有写回主稿。

不要声称“完成”“定稿”“引用已验证”或“可投稿”，除非相应检查已经运行并支持这个结论。
