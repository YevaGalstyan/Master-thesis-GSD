# Master's Thesis - Synthetic Price Path Generation for European Gas Markets

LaTeX source for the Master's thesis *Synthetic Price Path Generation for European Gas Markets Using Generative Adversarial Networks with Applications to Option Pricing*.

Yeva Galstyan · Department of Applied Computer Science, Fulda University of Applied Sciences
Supervisor: Prof. Dr. Christoph Scheich · Co-supervisor: Dr. Alexander Jungwirth

This repository contains the thesis document only. The data pipeline, model training, and evaluation code are maintained separately.

## Repository structure

```
main.tex                    Document root — includes everything below
literatur.bib               Bibliography, auto-exported from Zotero
content/
  preamble.tex              Packages, formatting, thesis setup
  titlepage.tex
  abstract.tex
  01_introduction.tex
  02_fundamentals/          Chapter 2, split by section
  03_methodology/           Chapter 3, split by section
  04_experiments.tex
  05_discussion.tex
  06_conclusion.tex
  appendix.tex
  ai_documentation.tex      Required documentation of AI tool usage
  declaration.tex           Declaration of authorship
figures/                    Figures included in the document
assets/                     Institutional logo and template assets
```

Build artifacts (`main.aux`, `main.log`, `main.toc`, and similar) are generated on every compile and are excluded via `.gitignore`.

## Building

Requires a TeX distribution with `latexmk` and `biber`. On macOS, MacTeX provides both.

```bash
latexmk -pdf main.tex
```

The bibliography uses BibLaTeX with the Biber backend, so `latexmk` runs the extra passes automatically. To clear all generated files:

```bash
latexmk -C
```

## Local setup

### TeX distribution

Install MacTeX, either from [tug.org/mactex](https://tug.org/mactex/) or via Homebrew:

```bash
brew install --cask mactex
```

The installer requires admin rights — watch for the password prompt, as the install silently does nothing if it is missed. Open a new terminal afterwards and confirm:

```bash
which latexmk biber
```

Both should resolve under `/Library/TeX/texbin/`.

### VS Code

Install the **LaTeX Workshop** extension (James Yu). Recommended additions: **Code Spell Checker** and **LTeX+** for prose checking.

Workspace settings live in `.vscode/settings.json`:

```json
{
  "latex-workshop.latex.path": "/Library/TeX/texbin",
  "latex-workshop.latex.recipe.default": "latexmk",
  "latex-workshop.latex.autoBuild.run": "onSave",
  "latex-workshop.view.pdf.viewer": "tab",
  "editor.wordWrap": "on",
  "cSpell.language": "en-US",
  "ltex.language": "en-US"
}
```

The default recipe must be `latexmk` (pdfLaTeX). The document uses Type 1 Palatino, which LuaLaTeX cannot resolve — building with the LuaLaTeX recipe fails on missing glyphs, including the euro sign.

Build with `LaTeX Workshop: Build LaTeX project` from the Command Palette; preview with `Ctrl/Cmd+Alt+V`.

### Bibliography

`literatur.bib` is auto-exported from Zotero via Better BibTeX. To reconnect on a new machine:

1. Right-click the `thesis` collection in Zotero → **Export Collection...**
2. Format: **Better BibTeX**, with **Keep updated** enabled
3. Save as `literatur.bib` in the repository root

Existing auto-exports can be managed under Zotero → Settings → Better BibTeX → Automatic export. Note that exports only run while Zotero is open.

Reference metadata is edited in Zotero, never directly in `literatur.bib` — the file is overwritten on every export.

## Conventions

- American English spelling throughout
- Citation keys follow `authorYEARkeyword`
- `\textcite` where the author is the subject of the sentence, `\parencite` otherwise
- Passive past tense for methodological decisions, present tense for architectural and definitional descriptions
- Chapters are split into per-section files under `content/`

## Data

The TTF futures data (Bloomberg, via BASF) and the ICE TTF options data (Databento) are licensed and are not included in this repository. Processing steps are documented in the methodology chapter and are reproducible given access to the same sources.

## Status

Private repository during the writing period. Publication after submission is under consideration.