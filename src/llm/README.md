# LLM Module

## Overview

The LLM module provides a unified interface for interacting with Large Language Models (LLMs) used throughout CyberGuardian AI.

The module follows the **Factory Design Pattern**, allowing the application to switch between different providers without changing the rest of the codebase.

Current provider:

- Groq

Future supported providers:

- OpenRouter
- Ollama
- Gemini
- OpenAI

---

# Folder Structure

```
llm/

├── __init__.py
├── base_llm.py
├── groq_llm.py
├── llm_factory.py
├── test.py
└── README.md
```

---

# Components

## base_llm.py

Defines the abstract interface that every LLM provider must implement.

```python
generate(prompt: str) -> str
```

All providers inherit from this class.

---

## groq_llm.py

Production implementation using the Groq API.

Responsibilities:

- API communication
- System prompt injection
- Error handling
- Response generation

---

## llm_factory.py

Creates the appropriate LLM provider based on the project configuration.

Example:

```python
from src.llm.llm_factory import LLMFactory

llm = LLMFactory.create()
```

No other part of the project directly instantiates provider classes.

---

## test.py

Tests the complete LLM module.

Coverage:

- Base Interface
- Groq Provider
- Factory
- End-to-End Generation

Run:

```bash
python -m src.llm.test
```

---

# Environment Variables

Required:

```
GROQ_API_KEY=
MODEL_NAME=
LLM_PROVIDER=groq
```

---

# Architecture

```
                config.py
                     │
                     ▼
              LLMFactory
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
     GroqLLM              Future Providers
         │
         ▼
      BaseLLM
```

---

# Usage

```python
from src.llm.llm_factory import LLMFactory

llm = LLMFactory.create()

response = llm.generate(
    "Explain DDoS Attack."
)

print(response)
```

---

# Design Principles

- Object-Oriented Design
- Factory Pattern
- Provider Independence
- Dependency Inversion
- Single Responsibility Principle
- Easy Extensibility

---

# Status

| Component | Status |
|----------|--------|
| BaseLLM | ✅ |
| Groq Provider | ✅ |
| Factory | ✅ |
| Testing | ✅ |
| Documentation | ✅ |

---

CyberGuardian AI