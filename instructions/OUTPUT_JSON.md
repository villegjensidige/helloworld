# Required JSON Format

Your final output must be saved as `analysis.json` and contain ONLY valid JSON. Do not wrap it in markdown code blocks.

{
  "patient_name": "Extracted name or null",
  "procedure": "Extracted procedure",
  "status": "Approved | Denied | Manual Review Required",
  "reasoning": "A short, 1-sentence explanation of why this status was chosen based on the register and exceptions."
}