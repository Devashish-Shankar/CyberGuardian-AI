# Knowledge Module

## Overview

The **Knowledge Module** is responsible for transforming machine learning predictions into structured cybersecurity intelligence.

Instead of returning only an attack label (e.g., `DDoS`), this module retrieves comprehensive information about the attack, including:

- Attack category
- Severity level
- Description
- Indicators of Compromise (IoCs)
- Detection logic
- MITRE ATT&CK mappings
- Mitigation strategies
- Network protocols
- Common ports
- References

This module acts as the **knowledge layer** of CyberGuardian AI and is consumed by the LLM, AI Agents, Incident Report Generator, and Dashboard.

---

# Module Architecture

```
                       attacks.json
                             │
                             ▼
                  KnowledgeLoader
                             │
                             ▼
                   AttackDatabase
                             │
             ┌───────────────┴───────────────┐
             ▼                               ▼
      AttackMapper                  SeverityEngine
             │                               │
             ├───────────────┬───────────────┤
             ▼               ▼               ▼
      MitigationEngine   MitreLoader   Future Modules
```

---

# Folder Structure

```
knowledge/

├── __init__.py
├── attack_database.py
├── attack_mapper.py
├── knowledge_loader.py
├── mitigation.py
├── mitre_loader.py
├── severity.py
├── test.py
└── README.md
```

---

# Responsibilities

## attack_database.py

Provides a high-level interface to the cybersecurity knowledge base.

### Responsibilities

- Load attack database
- Store attack objects
- Retrieve attack by name
- Check attack existence
- Return all available attacks

---

## knowledge_loader.py

Responsible for loading the JSON knowledge base.

### Responsibilities

- Read attacks.json
- Validate file existence
- Return Python dictionary

---

## attack_mapper.py

Maps an ML prediction to a complete attack object.

### Example

Input

```python
"DDoS"
```

Output

```python
{
    "category": "...",
    "severity": "...",
    "description": "...",
    ...
}
```

---

## severity.py

Returns the severity level of an attack.

Example

```python
Critical
```

---

## mitigation.py

Returns mitigation recommendations.

Example

```python
[
    "Enable WAF",
    "Rate Limiting",
    "Deploy CDN"
]
```

---

## mitre_loader.py

Returns MITRE ATT&CK Technique IDs.

Example

```python
[
    "T1498"
]
```

---

# Knowledge Base

The knowledge base is stored in

```
data/
└── knowledge/
      attacks.json
```

Currently supported attacks:

- Benign
- DDoS
- DoS Hulk
- DoS GoldenEye
- DoS Slowloris
- DoS Slowhttptest
- PortScan
- Bot
- FTP-Patator
- SSH-Patator
- Web Attack Brute Force
- Web Attack XSS
- Web Attack SQL Injection
- Infiltration
- Heartbleed

Total Attacks

```
15
```

---

# Public APIs

## Load Database

```python
db = AttackDatabase()
```

---

## Get Attack

```python
attack = db.get("DDoS")
```

---

## Check Attack

```python
db.exists("DDoS")
```

Returns

```python
True
```

---

## Get Severity

```python
severity = SeverityEngine().get(attack)
```

---

## Get Mitigation

```python
mitigation = MitigationEngine().get(attack)
```

---

## Get MITRE Mapping

```python
MitreLoader().get(attack)
```

---

# Example Workflow

```
Prediction
      │
      ▼
"DDoS"
      │
      ▼
AttackMapper
      │
      ▼
Attack Object
      │
      ├────────► Severity Engine
      │
      ├────────► MITRE Loader
      │
      ├────────► Mitigation Engine
      │
      ▼
Structured Cybersecurity Knowledge
```

---

# Testing

Run

```bash
python -m src.knowledge.test
```

Expected Output

```
Testing Attack Database
✓ Passed

Testing Knowledge Loader
✓ Passed

Testing Attack Mapper
✓ Passed

Testing Severity Engine
✓ Passed

Testing Mitigation Engine
✓ Passed

Testing MITRE Loader
✓ Passed
```

---

# Dependencies

- Python 3.12+
- Standard Library
  - json
  - pathlib

No external packages are required.

---

# Design Principles

The Knowledge Module follows the **Single Responsibility Principle (SRP)**.

Each file has exactly one responsibility:

| Module | Responsibility |
|----------|---------------|
| attack_database.py | Database interface |
| knowledge_loader.py | JSON loader |
| attack_mapper.py | Attack mapping |
| severity.py | Severity retrieval |
| mitigation.py | Mitigation retrieval |
| mitre_loader.py | MITRE mapping |

This design keeps the module modular, testable, and easy to extend.

---

# Future Integration

The Knowledge Module will be consumed by:

- Explainability Module
- LLM Layer
- Multi-Agent System
- Incident Report Generator
- Streamlit Dashboard
- FastAPI Backend

---

# Status

| Component | Status |
|-----------|--------|
| Attack Database | ✅ Complete |
| Knowledge Loader | ✅ Complete |
| Attack Mapper | ✅ Complete |
| Severity Engine | ✅ Complete |
| Mitigation Engine | ✅ Complete |
| MITRE Loader | ✅ Complete |
| Knowledge Base | ✅ Complete |

---

**Module Status:** ✅ Complete