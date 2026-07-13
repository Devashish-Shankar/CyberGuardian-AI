# Explainability Module

## Overview

The **Explainability Module** provides transparent and interpretable explanations for machine learning predictions made by CyberGuardian AI.

Instead of simply predicting whether a network flow is malicious, this module explains:

- Why the model made the prediction
- Which features influenced the decision
- Feature importance ranking
- Human-readable explanation
- Professional SHAP visualizations

This module enables analysts to understand, validate, and trust the model's decisions.

---

# Module Architecture

```
                   Network Flow
                         │
                         ▼
                 Trained ML Model
                         │
                         ▼
                 SHAP Explainer
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
      Feature Importance      SHAP Values
              │                     │
              ▼                     ▼
      Feature Ranker         Visualization
              │                     │
              └──────────┬──────────┘
                         ▼
                Narrative Builder
                         │
                         ▼
               Human Explanation
```

---

# Folder Structure

```
explainability/

├── __init__.py
├── shap_explainer.py
├── feature_ranker.py
├── narrative_builder.py
├── visualization.py
├── test_shap.py
└── README.md
```

---

# Responsibilities

## shap_explainer.py

Generates SHAP values for a single prediction.

### Responsibilities

- Load trained model
- Initialize SHAP TreeExplainer
- Generate SHAP values
- Support SHAP 0.52+
- Return feature contributions

---

## feature_ranker.py

Ranks features according to their SHAP contribution.

### Responsibilities

- Compute absolute SHAP importance
- Sort features
- Return Top-K important features

Example

```
Flow Duration
Destination Port
Packet Length Mean
Flow Bytes/s
...
```

---

## narrative_builder.py

Converts feature importance into a human-readable explanation.

Example

```
The model classified this traffic as malicious primarily because
Flow Duration, Destination Port, and Packet Length Mean had the
largest influence on the prediction.
```

---

## visualization.py

Creates professional SHAP visualizations.

Generated files

```
artifacts/shap/

bar_plot.png

waterfall_plot.png

force_plot.html
```

---

# Generated Outputs

```
artifacts/

└── shap/

    ├── bar_plot.png

    ├── waterfall_plot.png

    └── force_plot.html
```

---

# Public APIs

## SHAP Explainer

```python
explainer = SHAPExplainer(
    "artifacts/models/rf_binary.pkl"
)

values = explainer.explain(sample)
```

---

## Feature Ranking

```python
ranker = FeatureRanker()

ranking = ranker.rank(
    sample,
    values,
    top_k=10
)
```

---

## Narrative Generation

```python
builder = NarrativeBuilder()

text = builder.build(ranking)
```

---

## Visualization

```python
visualizer = SHAPVisualizer()

visualizer.generate_all(
    explainer,
    values,
    sample
)
```

---

# Explainability Workflow

```
Network Flow
      │
      ▼
Random Forest Prediction
      │
      ▼
SHAP Explainer
      │
      ▼
SHAP Values
      │
      ├────────► Feature Ranker
      │
      ├────────► Narrative Builder
      │
      └────────► Visualization
                    │
                    ▼
         Explainable Prediction
```

---

# Example Workflow

```python
from src.explainability.shap_explainer import SHAPExplainer
from src.explainability.feature_ranker import FeatureRanker
from src.explainability.narrative_builder import NarrativeBuilder
from src.explainability.visualization import SHAPVisualizer

explainer = SHAPExplainer(
    "artifacts/models/rf_binary.pkl"
)

values = explainer.explain(sample)

ranking = FeatureRanker().rank(
    sample,
    values,
    top_k=10
)

narrative = NarrativeBuilder().build(
    ranking
)

SHAPVisualizer().generate_all(
    explainer,
    values,
    sample
)
```

---

# Testing

Run

```bash
python -m src.explainability.test_shap
```

Expected Output

```
Loading dataset...
✓ Dataset Loaded

Loading model...
✓ Model Loaded

Testing SHAP Explainer...
✓ Passed

Testing Feature Ranker...
✓ Passed

Testing Narrative Builder...
✓ Passed

Testing SHAP Visualizer...
✓ Passed

All Explainability Tests Passed
```

---

# Dependencies

- Python 3.12+
- SHAP >= 0.52
- NumPy
- Pandas
- Matplotlib
- Joblib
- Scikit-learn

---

# Design Principles

The Explainability Module follows the **Single Responsibility Principle (SRP)**.

| Module | Responsibility |
|----------|---------------|
| shap_explainer.py | Generate SHAP values |
| feature_ranker.py | Rank important features |
| narrative_builder.py | Generate explanation |
| visualization.py | Generate SHAP visualizations |

Each component performs exactly one task, making the module modular, testable, and maintainable.

---

# Integration

The Explainability Module is consumed by:

- Knowledge Module
- LLM Layer
- AI Agents
- Incident Report Generator
- Streamlit Dashboard
- FastAPI Backend

---

# Future Improvements

Planned enhancements include:

- Global SHAP summary analysis
- Batch explainability for multiple samples
- Interactive dashboard visualizations
- PDF explanation reports
- Explainability caching
- Multi-model support (XGBoost, LightGBM, CatBoost)

---

# Status

| Component | Status |
|-----------|--------|
| SHAP Explainer | ✅ Complete |
| Feature Ranker | ✅ Complete |
| Narrative Builder | ✅ Complete |
| Visualization | ✅ Complete |
| SHAP Test Suite | ✅ Complete |

---

# Summary

The Explainability Module transforms raw machine learning predictions into transparent, interpretable insights by combining SHAP explanations, feature ranking, narrative generation, and visual analytics.

This enables security analysts to understand not only **what** the model predicted, but also **why** it reached that decision, improving trust, debugging, and incident response.

---

**Module Status:** ✅ Complete