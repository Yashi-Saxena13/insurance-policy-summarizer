# Policy Summarizer CLI

A Python command-line application that extracts important information from insurance policy documents using Large Language Models.

## Features

- Reads policy documents from text files
- Extracts key policy details
- Verifies completeness using a second LLM pass
- Saves results as JSON
- Automatic Gemini → Groq fallback using LiteLLM

## Project Structure

```text
project/
│
├── main.py
├── extractor.py
├── verifier.py
├── prompts.py
├── llm.py
├── utils.py
│
├── policies/
│   ├── policy1.txt
│   ├── policy2.txt
│   └── policy3.txt
│
├── output/
│   └── output.json
│
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file containing:

```
GEMINI_API_KEY=your_key
GROQ_API_KEY=your_key
```

## Usage

```bash
python main.py policies/policy1.txt
```

The verified summary is saved to:

```
output/output.json
```

## Technologies

- Python
- LiteLLM
- Google Gemini 2.5 Flash
- Groq Llama 3.3