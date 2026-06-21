import sys

from extractor import (
    generate_summary,
    extract_coverage_limits,
    extract_exclusions,
)

from verifier import verify_summary
from utils import save_summary


def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <policy_file>")
        return

    filename = sys.argv[1]

    try:

        with open(filename, "r", encoding="utf-8") as f:
            policy_text = f.read()

        print("📄 Reading policy...")

        # --------------------------------------------------
        # Step 1 - Summary
        # --------------------------------------------------
        print("📝 Generating summary...")
        summary = generate_summary(policy_text)

        # --------------------------------------------------
        # Step 2 - Coverage Limits
        # --------------------------------------------------
        print("💰 Extracting coverage limits...")
        coverage = extract_coverage_limits(policy_text)

        # --------------------------------------------------
        # Step 3 - Exclusions
        # --------------------------------------------------
        print("🚫 Extracting exclusions...")
        exclusions = extract_exclusions(policy_text)

        # --------------------------------------------------
        # Step 4 - Verification
        # --------------------------------------------------
        print("✅ Verifying outputs...")

        verified = verify_summary(
            policy_text,
            summary,
            coverage,
            exclusions,
        )

        # --------------------------------------------------
        # Print Results
        # --------------------------------------------------
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(summary)

        print("\n" + "=" * 60)
        print("COVERAGE LIMITS")
        print("=" * 60)
        print(coverage)

        print("\n" + "=" * 60)
        print("EXCLUSIONS")
        print("=" * 60)
        print(exclusions)

        print("\n" + "=" * 60)
        print("SELF VERIFICATION")
        print("=" * 60)
        print(verified)

        # Save verification output
        save_summary(verified)

        print("\n🎉 Done!")

    except FileNotFoundError:
        print(f"❌ File not found: {filename}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()