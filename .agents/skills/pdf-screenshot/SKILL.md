---
name: pdf-screenshot
description: >-
  Use this skill to extract figures or tables from PDF files as high-quality images and insert them into LaTeX documents.
---

# PDF Screenshot Skill

This skill provides a pipeline to extract a specific figure or table from a PDF research paper, crop it using the Gemini vision API, save it to the `figures/` directory, and integrate it into the LaTeX monograph files.

## Workflow

To extract a figure and insert it into a LaTeX file, follow these steps:

### 1. Execute the Extraction Script
Run the helper Python script located at `scripts/extract_figure.py` in this skill directory:
```bash
python3 .agents/skills/pdf-screenshot/scripts/extract_figure.py \
  --pdf "<pdf_path>" \
  --label "<figure_label_or_number>" \
  --keywords "<comma_separated_keywords_to_locate_page>" \
  --caption "<full_figure_caption_for_gemini_detection>" \
  --output "figures/<desired_output_name>.png"
```

### 2. Verify Output
Check that the figure is successfully cropped and saved under the `figures/` directory.

### 3. Update LaTeX Monograph
Locate the corresponding placeholder in the `.tex` files (e.g., `sections/chapter2.tex` or `sections/introduction.tex`) and replace the placeholder tag with a standard LaTeX figure block:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/<figure_name>.png}
    \caption{<Caption text> \cite{<citation_key>}.}
    \label{fig:<label_key>}
\end{figure}
```
