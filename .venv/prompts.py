"""
prompts.py

Contains all prompts used by the P&C Policy Summariser CLI Tool.

Assignment Requirements:
1. Chain-of-Thought prompting for Summary
2. Few-shot prompting for Coverage Extraction
3. Exclusions Extraction
4. Self Verification
"""

# ==========================================================
# 1. SUMMARY PROMPT (Chain-of-Thought)
# ==========================================================

SUMMARY_PROMPT = """
You are an expert Property & Casualty Insurance Analyst.

Your task is to read the insurance policy carefully.

Think step by step about:
1. What type of insurance policy this is.
2. What risks are covered.
3. Important coverage limits.
4. Major exclusions.
5. Important conditions or deductibles.

After reasoning internally, DO NOT show your reasoning.

Return ONLY a plain-English summary as EXACTLY FIVE bullet points.

Insurance Policy:

{policy}
"""


# ==========================================================
# 2. COVERAGE EXTRACTION PROMPT (Few-Shot)
# ==========================================================

EXTRACTION_PROMPT = """
You are an insurance information extraction assistant.

Extract ALL coverage items, sums insured, deductibles, waiting periods, and premiums.
If a coverage item has no amount, use "Covered" as the value.

Return ONLY valid JSON. No markdown, no explanation — raw JSON only.

Example 1

Policy:

Coverage A (Dwelling): $300,000
Other Structures: $20,000
Personal Property: $100,000
Deductible: $1,000

Output:

{{
  "Coverage A (Dwelling)": "$300,000",
  "Other Structures": "$20,000",
  "Personal Property": "$100,000",
  "Deductible": "$1,000"
}}


Example 2

Policy:

Medical emergencies: ₹10 lakh
Trip cancellation: Covered
Lost baggage: Covered
Waiting period: 7 days
Premium: ₹4,200

Output:

{{
  "Medical emergencies": "₹10 lakh",
  "Trip cancellation": "Covered",
  "Lost baggage": "Covered",
  "Waiting period": "7 days",
  "Premium": "₹4,200"
}}


Now extract from this policy.

Policy:

{policy}
"""


# ==========================================================
# 3. EXCLUSION EXTRACTION PROMPT
# ==========================================================

EXCLUSION_PROMPT = """
You are an insurance policy analyst.

Read the insurance policy carefully.

Extract every policy exclusion.

Return ONLY a bullet list.

Insurance Policy:

{policy}
"""


# ==========================================================
# 4. SELF VERIFICATION PROMPT
# ==========================================================

VERIFY_PROMPT = """
You are an insurance policy auditor.

You will be given an original policy and some generated outputs.
Follow these steps EXACTLY:

STEP 1 — Re-extract independently from the policy:
Without looking at the generated outputs, extract these yourself:
a) List every PRIMARY coverage item and its EXACT limit
b) List every MAJOR exclusion (ignore minor admin exclusions)
c) Note only restrictions that significantly affect a claim
   (e.g. outbound only, electronics excluded, sub-limits)
d) Note claim deadlines only if multiple different deadlines exist

STEP 2 — Compare your extraction to the generated outputs:
Check the generated Summary, Coverage JSON, and Exclusions against
your own extraction from Step 1.

Flag as INCORRECT only if:
- A rupee amount or limit is factually wrong (not just missing)
- An exclusion is stated in a way that CONTRADICTS the policy
- Something appears in outputs that is NOT in the policy at all

Flag as MISSING only if:
- A PRIMARY coverage limit is completely absent from Coverage JSON
- A MAJOR exclusion is completely absent from the Exclusions list
- A restriction that would DIRECTLY cause a claim to be rejected
  is missing (e.g. electronics excluded from baggage, outbound only)

Do NOT flag:
- Policy numbers, insured names, policy period
- Claim process steps or helpline numbers
- Admin conditions like grace period or renewal terms
- Minor sub-limits that are supplementary to main coverage
- Partial details when the main point is correctly captured

STEP 3 — Give your verdict:
PASS if all primary coverage limits are correct and present,
all major exclusions are captured without contradiction, and
no hallucinated information exists in the outputs.

FAIL only if a rupee figure is factually wrong, a major exclusion
directly contradicts the policy, a claim-critical restriction is
missing, or hallucinated information appears in the outputs.

═══════════════════════════════════════════════════════
Original Policy:
{policy}

═══════════════════════════════════════════════════════
Generated Summary:
{summary}

═══════════════════════════════════════════════════════
Coverage JSON:
{details}

═══════════════════════════════════════════════════════
Extracted Exclusions:
{exclusions}

═══════════════════════════════════════════════════════

Return your answer in this EXACT format:

My Extraction (Step 1):
[Your independent extraction here]

Comparison (Step 2):
[Your comparison findings here]

Verification Status:
PASS
or
FAIL

Explanation:
- List each issue with exact reference to policy vs output
- If no issues found, confirm outputs accurately represent the policy
"""