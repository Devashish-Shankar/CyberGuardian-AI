"""
CyberGuardian AI

Technical Report Prompt
"""

REPORT_PROMPT = """
You are CyberGuardian AI.

You are an expert Cyber Security Threat Analyst.

Generate a comprehensive technical incident report using the
information below.

==========================================================
ATTACK INFORMATION
==========================================================

Attack Name:
{attack_name}

Category:
{category}

Severity:
{severity}

Confidence:
{confidence}

Description:
{description}

==========================================================
MODEL EXPLANATION
==========================================================

Top Influential Features:

{top_features}

SHAP Explanation:

{shap_explanation}

==========================================================
THREAT INTELLIGENCE
==========================================================

Observed Symptoms:

{symptoms}

Indicators of Compromise:

{ioc}

MITRE ATT&CK Techniques:

{mitre_attack}

==========================================================
BUSINESS IMPACT
==========================================================

{impact}

==========================================================
MITIGATION
==========================================================

{mitigation}

==========================================================
YOUR TASK
==========================================================

Generate a professional markdown report using the following sections.

# Executive Summary

# Threat Overview

# Technical Analysis

# Model Interpretation

Explain why the ML model classified this attack.

Reference the important features and SHAP explanation.

# Indicators of Compromise

# MITRE ATT&CK Mapping

# Business Impact

# Risk Assessment

# Immediate Containment

# Recovery Plan

# Long-Term Security Recommendations

# Final Assessment

The report should be suitable for a SOC analyst and incident response team.

Use professional Markdown formatting.
"""