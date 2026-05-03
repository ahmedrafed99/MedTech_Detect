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
        B["Preprocessing - Drop ID & Insurance - Neg→0 / Pos→1"]
        C["Train / Test Split - 80% train · 20% test"]
        D["Logistic Regression - model.fit()"]
        A --> B --> C --> D
    end

    D --> E

    subgraph MODEL ["Persisted Model"]
        E[("sepsis_model.sav - joblib")]
    end

    E --> G

    subgraph INFER ["② Inference Pipeline"]
        direction LR
        F["HTTP Client - POST /predict/patient"]
        G["FastAPI Router - routes/routes.py"]
        H["Load Model - joblib.load()"]
        I["predict_sepsis() - model.predict(df)"]
        J{{"Result: 0=Negative · 1=Positive"}}
        F --> G --> H --> I --> J
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
├── main.py                    ← FastAPI app entry point
├── routes/routes.py           ← /health + /predict/patient endpoints
├── model/training_model.py    ← train + save + predict_sepsis()
├── parser/preprocessing.py    ← drop columns, encode target
├── data/data_sepsis.csv       ← 608 ICU patient records
└── model/sepsis_model.sav     ← saved logistic regression (joblib)
```
