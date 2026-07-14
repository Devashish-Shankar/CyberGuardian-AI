# Prompts Module

## Overview

The **Prompts Module** contains all reusable prompt templates used by CyberGuardian AI.

Instead of embedding prompts directly inside the application logic, every prompt is isolated into dedicated files. This keeps the codebase modular, maintainable, and easy to extend.

The prompts are consumed by the LLM layer and AI agents to generate professional cybersecurity analyses, incident reports, executive summaries, and technical explanations.

---

# Module Architecture

```
                 Knowledge Layer
                        │
                        ▼
                Prompt Templates
                        │
                        ▼
                   LLM Provider
                        │
                        ▼
              AI Generated Response
```

---

# Folder Structure

```
prompts/

├── __init__.py
├── security_prompt.py
├── analyst_prompt.py
├── incident_prompt.py
├── executive_prompt.py
├── report_prompt.py
├── summary_prompt.py
├── test.py
└── README.md
```

---

# Components

## security_prompt.py

Defines the global system prompt used by every LLM request.

Responsibilities

- Define AI personality
- Prevent hallucinations
- Enforce cybersecurity context
- Standardize response style

---

## analyst_prompt.py

Generates detailed SOC analyst explanations.

Includes:

- Attack analysis
- ML interpretation
- Business impact
- Feature explanation
- Mitigation

---

## incident_prompt.py

Generates professional incident reports.

Sections include:

- Executive Summary
- Technical Analysis
- IoCs
- MITRE ATT&CK Mapping
- Risk Assessment
- Recovery Plan

---

## executive_prompt.py

Creates executive-level cybersecurity briefings.

Designed for:

- CEO
- CTO
- CISO
- Management

Focuses on:

- Business risk
- Financial impact
- Strategic recommendations

---

## report_prompt.py

Master technical report template.

Combines:

- ML prediction
- SHAP explanation
- Threat intelligence
- MITRE mapping
- Business impact
- Recommendations

---

## summary_prompt.py

Creates concise summaries suitable for:

- Dashboard cards
- Alert notifications
- Email summaries
- Slack/Teams alerts

---

# Prompt Workflow

```
Network Traffic
        │
        ▼
ML Prediction
        │
        ▼
Knowledge Layer
        │
        ▼
Prompt Template
        │
        ▼
Groq LLM
        │
        ▼
Generated Response
```

---

# Testing

Run

```bash
python -m src.prompts.test
```

Expected Output

```
Testing Security Prompt
✓ Passed

Testing Analyst Prompt
✓ Passed

Testing Incident Prompt
✓ Passed

Testing Executive Prompt
✓ Passed

Testing Report Prompt
✓ Passed

Testing Summary Prompt
✓ Passed

ALL PROMPT TESTS PASSED
```

---

# Design Principles

The Prompts Module follows the **Single Responsibility Principle (SRP)**.

Each prompt serves exactly one purpose.

| Prompt | Responsibility |
|----------|----------------|
| security_prompt.py | Global system prompt |
| analyst_prompt.py | Technical analysis |
| incident_prompt.py | Incident report |
| executive_prompt.py | Executive briefing |
| report_prompt.py | Detailed technical report |
| summary_prompt.py | Short summary |

---

# Integration

The Prompts Module is used by:

- LLM Module
- AI Agents
- Incident Report Generator
- Dashboard
- FastAPI Backend

---

# Future Improvements

Potential future additions:

- Threat Hunting Prompt
- Malware Analysis Prompt
- IOC Extraction Prompt
- CVE Explanation Prompt
- Compliance Report Prompt
- Threat Intelligence Prompt

---

# Status

| Component | Status |
|-----------|--------|
| Security Prompt | ✅ Complete |
| Analyst Prompt | ✅ Complete |
| Incident Prompt | ✅ Complete |
| Executive Prompt | ✅ Complete |
| Report Prompt | ✅ Complete |
| Summary Prompt | ✅ Complete |
| Test Suite | ✅ Complete |
| Documentation | ✅ Complete |

---

# Summary

The Prompts Module centralizes every reusable prompt template used across CyberGuardian AI.

This separation ensures that prompt engineering remains independent from business logic, making the application easier to maintain, test, and extend.

---

**Module Status:** ✅ Complete