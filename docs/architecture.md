# MedTech Detect — Sepsis Prediction System

## Architecture

```mermaid
flowchart TD
    subgraph FEATURES ["Patient Input Features"]
        direction LR
        PRG["PRG: Pregnancies"]
        PL["PL: Plasma Glucose"]
        PR["PR: Blood Pressure"]
        SK["SK: Skin Thickness"]
        TS["TS: Insulin"]
        M11["M11: BMI"]
        BD2["BD2: Diab. Pedigree"]
        AGE["Age"]
    end

    FEATURES --> A

    subgraph TRAIN ["① Training Pipeline"]
        direction LR
        A[("data_sepsis.csv - 608 ICU patients")]
        B["Preprocessing - Drop ID & Insurance - cast to float - Neg→0 / Pos→1"]
        C["Train / Test Split - 80% train · 20% test"]
        D["train_model() - Logistic Regression - model.fit()"]
        A --> B --> C --> D
    end

    D --> E

    subgraph MODEL ["Persisted Model"]
        E[("sepsis_model.sav - joblib")]
    end

    E --> H

    subgraph INFER ["② Inference Pipeline"]
        direction LR
        F["Browser - GET /  - index.html form"]
        G["FastAPI Router - routes/routes.py - Static files mounted"]
        H["Load Model - joblib.load()"]
        I["predict_sepsis() - model.predict(df)"]
        J{{"JSON: Prediction 0 or 1"}}
        F -->|"POST /predict/patient - Form data float x8"| G --> H --> I --> J
    end
```

## Model Performance

```mermaid
flowchart LR
    subgraph OVERALL ["Overall"]
        ACC["Accuracy: 77.5%"]
    end

    subgraph NEG ["Class: Negative"]
        PN["Precision: 80%"]
        RN["Recall: 86%"]
        FN["F1: 0.83"]
    end

    subgraph POS ["Class: Positive"]
        PP["Precision: 71%"]
        RP["Recall: 63%"]
        FP["F1: 0.67"]
    end
```

> Test set: 120 patients (77 Negative · 43 Positive)

## File Map

```
MedTech_Detect/
├── main.py                    ← FastAPI app, mounts /static
├── routes/routes.py           ← GET / · GET /health · POST /predict/patient (Form)
├── model/training_model.py    ← train_model() · predict_sepsis()
├── parser/preprocessing.py    ← drop columns, cast to float, encode target
├── data/data_sepsis.csv       ← 608 ICU patient records
├── model/sepsis_model.sav     ← saved logistic regression (joblib)
├── static/style.css           ← frontend styles
├── static/script.js           ← frontend logic
├── templates/index.html       ← prediction form (Jinja2)
└── tests/                     ← app_test.py · routes_test.py
```
