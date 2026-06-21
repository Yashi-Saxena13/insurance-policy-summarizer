# ADR-001: P&C Policy Summariser CLI Tool

## Status
Accepted

## Project
Phase Gate 1 – P&C Policy Summariser CLI Tool

---

# Context

The objective of this project is to build a Python command-line application that processes a Property & Casualty (P&C) insurance policy document and generates:

1. A plain-English summary in five bullet points.
2. Key coverage limits in structured JSON format.
3. A list of policy exclusions.
4. A self-check that verifies the generated summary against the source document.

The solution should demonstrate prompt engineering techniques including Chain-of-Thought prompting and Few-Shot prompting.

---

# Architecture

```
                 Policy Document (.pdf/.txt)
                          │
                          ▼
                 extractor.py
          (Extract text from document)
                          │
                          ▼
                     prompts.py
          (Stores all LLM prompts)
                          │
                          ▼
                      llm.py
        (Calls Gemini API and returns output)
                          │
         ┌────────────────┼─────────────────┐
         ▼                ▼                 ▼
   Summary Prompt   Extraction Prompt   Verification Prompt
         │                │                 │
         ▼                ▼                 ▼
  5 Bullet Summary   Coverage JSON    Self-check Report
                          │
                          ▼
                      main.py
                 (CLI Entry Point)
```

---

# Design Decisions

## 1. Python CLI

A command-line interface was selected because the assignment specifically requires a CLI application. It is lightweight, easy to demonstrate, and allows different policy documents to be tested quickly.

---

## 2. Chain-of-Thought Prompting for Summarisation

The summarisation prompt encourages the language model to reason through the policy before generating the final summary.

Reason:
- Produces more coherent summaries.
- Helps identify important clauses.
- Reduces the chance of missing critical information.

The application only displays the final summary and not the reasoning.

---

## 3. Few-Shot Prompting for Information Extraction

Few-shot examples were included for extracting:

- Coverage limits
- Deductibles
- Exclusions

Reason:
- Produces consistent JSON output.
- Improves extraction accuracy across different policy formats.
- Reduces formatting inconsistencies.

---

## 4. Self-Verification Step

After generating the summary, the model is prompted again to compare the generated output against the original policy.

Purpose:
- Detect hallucinations.
- Identify missing information.
- Improve reliability.

---

# Technologies Used

- Python 3.11
- Google Gemini API
- PyPDF2
- python-dotenv
- JSON
- Git & GitHub

---

# Prompt Design

Three separate prompts are used:

### Summary Prompt
Generates a five-bullet plain-English summary using Chain-of-Thought reasoning.

### Extraction Prompt
Uses Few-Shot examples to extract:
- Coverage limits
- Deductibles
- Exclusions

Outputs structured JSON.

### Verification Prompt
Compares the generated summary with the original policy and reports inconsistencies.

---

# Challenge Encountered

### Issue

Initially, `prompts.py` was mistakenly created inside the `.venv` directory and the virtual environment was accidentally committed to GitHub.

### Resolution

- Moved `prompts.py` to the project root.
- Added `.venv/` to `.gitignore`.
- Removed the virtual environment from Git tracking.
- Recreated the virtual environment and installed dependencies using `requirements.txt`.

This resulted in a cleaner project structure and repository.

---

# Future Improvements

- Support additional document formats.
- Add confidence scores for extracted information.
- Support multiple LLM providers.
- Export results to CSV or Excel.
- Develop a web interface using Streamlit.

---

# Conclusion

The implemented solution satisfies all Phase Gate 1 requirements by:

- Processing insurance policy documents.
- Generating concise summaries.
- Extracting structured policy information.
- Listing exclusions.
- Performing a self-verification step.
- Demonstrating the use of Chain-of-Thought and Few-Shot prompting.