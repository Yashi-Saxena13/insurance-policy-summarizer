"""
extractor.py

Generates:
1. Plain-English Summary
2. Coverage Limits (JSON)
3. Exclusions
"""

import re

from llm import ask
from prompts import (
    SUMMARY_PROMPT,
    EXTRACTION_PROMPT,
    EXCLUSION_PROMPT,
)


def _strip_fences(text: str) -> str:
    """Remove markdown code fences the LLM often wraps around output."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_summary(policy_text: str) -> str:
    """
    Generate a 5-bullet plain-English summary.
    Uses Chain-of-Thought prompting.
    """

    prompt = SUMMARY_PROMPT.format(policy=policy_text)

    response = ask(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    return response.choices[0].message.content


def extract_coverage_limits(policy_text: str) -> str:
    """
    Extract coverage limits as JSON.
    Uses Few-shot prompting.
    """

    prompt = EXTRACTION_PROMPT.format(policy=policy_text)

    response = ask(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    return _strip_fences(response.choices[0].message.content)  # strip fences


def extract_exclusions(policy_text: str) -> str:
    """
    Extract policy exclusions.
    """

    prompt = EXCLUSION_PROMPT.format(policy=policy_text)

    response = ask(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    return response.choices[0].message.content