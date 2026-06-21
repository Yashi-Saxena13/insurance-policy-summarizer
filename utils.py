import json
import os
from datetime import datetime


def save_summary(summary: str, filename: str = "output.json"):
    """
    Saves the verified summary to a JSON file inside the output/ folder.
    """

    os.makedirs("output", exist_ok=True)  # create folder if it doesn't exist

    filepath = os.path.join("output", filename)

    data = {
        "status": "success",
        "model": "Gemini 2.5 Flash (LiteLLM with Groq fallback)",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": summary
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✅ Summary saved to {filepath}")