# Agents Module

The **Agents Module** is the orchestration layer of **CyberGuardian AI**. It coordinates machine learning models, the cybersecurity knowledge base, explainability components, and Large Language Models (LLMs) to provide end-to-end AI-powered cyber threat detection and analysis.

Instead of allowing every module to communicate directly with one another, the Agents Module follows a modular architecture where each agent is responsible for a single task. This design improves maintainability, scalability, and testability.

---

# Objectives

The Agents Module is responsible for:

- Detecting whether incoming network traffic is malicious.
- Identifying the specific cyber attack.
- Retrieving structured cyber threat intelligence.
- Explaining model predictions using Explainable AI (SHAP).
- Generating professional SOC analyst reports.
- Generating detailed cybersecurity incident reports.
- Orchestrating the complete AI pipeline.

---

# Folder Structure

```text
src/
└── agents/
    ├── __pycache__/
    ├── README.md
    ├── test.py
    │
    ├── base_agent.py
    ├── prediction_agent.py
    ├── knowledge_agent.py
    ├── explainability_agent.py
    ├── analyst_agent.py
    ├── incident_agent.py
    └── supervisor_agent.py
```

---

# Module Architecture

```text
                     Network Traffic
                            │
                            ▼
                   Prediction Agent
                            │
              ┌─────────────┴─────────────┐
              │                           │
         Benign Traffic             Malicious Traffic
              │                           │
              ▼                           ▼
      Return Safe Status          Knowledge Agent
                                         │
                                         ▼
                               Explainability Agent
                                │                 │
                                ▼                 ▼
                         Analyst Agent     Incident Agent
                                │                 │
                                └────────┬────────┘
                                         ▼
                                Supervisor Response
```

---

# Agent Responsibilities

## 1. Base Agent

**File**

```text
base_agent.py
```

### Responsibility

Defines the common interface that every agent in the system follows.

### Public API

```python
run(...)
```

Every agent inherits from `BaseAgent`.

---

## 2. Prediction Agent

**File**

```text
prediction_agent.py
```

### Responsibility

Runs the trained machine learning models to detect attacks.

### Internal Workflow

```text
Network Sample
      │
      ▼
Binary Model

Attack?
      │
      ▼

Yes

↓

Multi-Class Model

↓

Attack Name
```

### Output

```python
{
    "is_attack": True,
    "attack_name": "DDoS",
    "confidence": 99.83,
    "top_predictions": [...]
}
```

---

## 3. Knowledge Agent

**File**

```text
knowledge_agent.py
```

### Responsibility

Retrieves structured cyber threat intelligence from the knowledge base.

### Uses

- Attack Mapper
- Severity Engine
- Mitigation Engine
- MITRE Loader

### Output

```python
{
    "attack_name": "...",
    "severity": "...",
    "description": "...",
    "symptoms": [...],
    "impact": "...",
    "mitigation": [...],
    "mitre_attack": [...],
    "ioc": [...],
    "references": [...]
}
```

---

## 4. Explainability Agent

**File**

```text
explainability_agent.py
```

### Responsibility

Generates Explainable AI insights.

### Uses

- SHAP Explainer
- Feature Ranker
- Narrative Builder
- SHAP Visualizer

### Output

```python
{
    "top_features": [...],
    "narrative": "...",
    "shap_values": [...],
    "visualization_generated": True
}
```

---

## 5. Analyst Agent

**File**

```text
analyst_agent.py
```

### Responsibility

Generates a professional SOC analyst report using the configured LLM.

### Uses

- LLM Factory
- Analyst Prompt

### Output

```markdown
# Executive Summary

...

# Technical Analysis

...

# Business Impact

...

# Recommendations
```

---

## 6. Incident Agent

**File**

```text
incident_agent.py
```

### Responsibility

Generates a complete cybersecurity incident report.

### Uses

- LLM Factory
- Report Prompt

### Output

```markdown
# Incident Summary

...

# Threat Details

...

# MITRE ATT&CK

...

# Recovery Plan
```

---

## 7. Supervisor Agent

**File**

```text
supervisor_agent.py
```

### Responsibility

Coordinates the complete AI workflow.

The Supervisor Agent never performs prediction, explainability, or report generation directly. It delegates each task to the appropriate agent.

### Workflow

```text
Prediction

↓

Knowledge

↓

Explainability

↓

Analyst

↓

Incident Report

↓

Final JSON Response
```

### Output

```python
{
    "status": "...",
    "prediction": {...},
    "knowledge": {...},
    "explainability": {...},
    "analysis": "...",
    "incident_report": "..."
}
```

---

# Agent Communication

```text
Prediction Agent
        │
        ▼
Knowledge Agent
        │
        ▼
Explainability Agent
        │
        ├──────────────┐
        ▼              ▼
Analyst Agent   Incident Agent
        │              │
        └──────┬───────┘
               ▼
      Supervisor Agent
```

---

# Design Principles

The Agents Module follows the following software engineering principles:

- Single Responsibility Principle (SRP)
- Separation of Concerns
- Dependency Injection
- Composition over Inheritance
- Loose Coupling
- High Cohesion
- Modular Design
- Production-Ready Architecture

---

# Testing

The module includes an integrated test suite.

**Test File**

```text
src/agents/test.py
```

The test suite validates:

- Base Agent
- Prediction Agent
- Knowledge Agent
- Explainability Agent
- Analyst Agent
- Incident Agent
- Supervisor Agent
- End-to-End AI Pipeline

Run the test suite using:

```bash
python -m src.agents.test
```

---

# Dependencies

The Agents Module depends on:

- Models Module
- Knowledge Module
- Explainability Module
- LLM Module
- Prompt Module
- Configuration Module

---

# Integration

The Agents Module is consumed by:

```text
FastAPI REST API

↓

Streamlit Dashboard

↓

External Applications
```

---

# Future Improvements

Planned enhancements include:

- Multi-Agent Collaboration
- Asynchronous Agent Execution
- Parallel Explainability Generation
- Multi-LLM Support
- Agent Memory
- Confidence Calibration
- Real-Time Streaming Responses
- Agent Performance Monitoring
- Distributed Execution
- Auto-Retry & Failure Recovery

---

# Module Status

| Component | Status |
|-----------|--------|
| Base Agent | ✅ Complete |
| Prediction Agent | ✅ Complete |
| Knowledge Agent | ✅ Complete |
| Explainability Agent | ✅ Complete |
| Analyst Agent | ✅ Complete |
| Incident Agent | ✅ Complete |
| Supervisor Agent | ✅ Complete |
| Integration Tests | ✅ Complete |
| Documentation | ✅ Complete |

---

# Summary

The Agents Module serves as the intelligent orchestration layer of CyberGuardian AI. It integrates machine learning, cybersecurity knowledge, explainable AI, and large language models into a unified workflow, enabling automated threat detection, explainability, professional analysis, and incident reporting through a modular and scalable architecture.