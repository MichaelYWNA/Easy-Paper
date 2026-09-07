# Installation Guide

This guide explains how to install Easy-Paper as a local Codex skill.

## Requirements

- Codex desktop or another agent environment that supports local skills.
- Git.
- Python 3.11 or newer for helper scripts.
- Internet access if you want OpenAlex or Crossref literature lookup.
- A LaTeX distribution such as TeX Live, MiKTeX, MacTeX or a journal-provided build environment if you want compile checks.

## Windows PowerShell

Install directly into the Codex skill folder:

```powershell
git clone https://github.com/MichaelYWNA/Easy-Paper.git "$env:USERPROFILE\.codex\skills\easy-paper"
```

Or install from a local clone:

```powershell
git clone https://github.com/MichaelYWNA/Easy-Paper.git
cd Easy-Paper
.\install.ps1
```

If PowerShell blocks script execution, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

## macOS / Linux

Install directly:

```bash
git clone https://github.com/MichaelYWNA/Easy-Paper.git ~/.codex/skills/easy-paper
```

Or install from a local clone:

```bash
git clone https://github.com/MichaelYWNA/Easy-Paper.git
cd Easy-Paper
bash install.sh
```

## Verify Installation

Open a new Codex task and type:

```text
$easy-paper
```

If the skill is available, Codex should load the Easy-Paper instructions.

You can also test the helper scripts:

```bash
python scripts/scholarly_search.py "typhoon wave height forecasting" --source openalex --limit 3
```

For a local LaTeX project:

```bash
python scripts/latex_project_inspect.py "path/to/latex-project"
```

## Update

If you installed by cloning directly into the skill folder:

```bash
cd ~/.codex/skills/easy-paper
git pull
```

On Windows:

```powershell
cd "$env:USERPROFILE\.codex\skills\easy-paper"
git pull
```

If you installed from a separate clone, pull the clone and rerun the install script.

## Uninstall

Remove the skill folder:

Windows PowerShell:

```powershell
Remove-Item -LiteralPath "$env:USERPROFILE\.codex\skills\easy-paper" -Recurse
```

macOS / Linux:

```bash
rm -rf ~/.codex/skills/easy-paper
```

## Common Problems

### Codex does not see `$easy-paper`

- Restart Codex or open a new task.
- Confirm the folder is named `easy-paper`.
- Confirm `SKILL.md` is directly inside that folder.

### Python script fails

- Check `python --version`.
- Use Python 3.11 or newer.
- If `python` points to another version, try `py -3.11` on Windows.

### Literature search is slow or rate-limited

- Start with small limits such as `--limit 10`.
- Prefer OpenAlex for broad discovery.
- Use DOI-based lookups when you already know the paper.
