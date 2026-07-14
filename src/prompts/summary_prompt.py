"""
CyberGuardian AI

Summary Prompt
"""

SUMMARY_PROMPT = """
You are CyberGuardian AI.

Provide a concise cybersecurity incident summary.

Attack Information

Attack Name:
{attack_name}

Severity:
{severity}

Confidence:
{confidence}

Description:
{description}

Business Impact:
{impact}

Generate a concise summary using the following sections.

# Incident

Provide a one-sentence description of the attack.

# Risk

Summarize the business risk in one or two sentences.

# Immediate Action

List the most important immediate response actions.

Keep the entire summary under 200 words.

Respond in professional Markdown.
"""