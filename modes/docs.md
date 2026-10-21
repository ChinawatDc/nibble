# nibble: Docs Mode (v0.2.0)

Specialized guidelines for processing documentation, PDFs, specifications, and data sheets.

## 1. Structural Navigation & Fallbacks
- **Scan Outlines First**: Read the Table of Contents, markdown headers (`#`, `##`), or PDF bookmark trees before fetching content.
- **IDE Fallback Strategy**: If the IDE lacks native outline/bookmark extraction APIs for binary formats (PDF, Word), fallback immediately:
  - Grep for section titles or keywords.
  - Read only the document preamble / first 30 lines.
  - Inspect summary sections before requesting broader pages.
- **Avoid Full Ingestion**: Never stream an entire manual into context when answering a targeted question. Read only the relevant section.

## 2. Concise Synthesis
- **Direct Answers**: Synthesize answers in bullet points. Do not quote verbatim paragraphs from the source material.
- **Reference Over Duplication**: State the document name, section number, or page index rather than reproducing long text passages.
- **Diff Specs**: When reviewing updated specs, extract only changed clauses or modified parameters.

## 3. Tabular & Structured Data
- **Header-Only Ingestion**: For large CSV or spreadsheet files, read line 1 (column names) and sample rows to understand the schema.
- **Filtered Slices**: Use shell commands (`awk`, `cut`, `grep`) or database queries to extract specific rows rather than reading thousands of lines.
