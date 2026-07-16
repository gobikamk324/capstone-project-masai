# Loan Risk Assessment – Part 2 (Model Training)

##  Models Trained
1. Baseline Model
   - Logistic Regression (benchmark model).

2. Advanced Models
   - Random Forest
   - XGBoost
   - LightGBM

3. Calibrated Models
   - Applied `CalibratedClassifierCV` (isotonic method) to Random Forest for probability reliability.
   - Evaluated calibration using Brier Score and reliability curves.

---

## Evaluation Metrics
- Classification Metrics: Accuracy, Precision, Recall, F1‑Score  
- Calibration Metric: Brier Score  
- Fairness Metrics: Approval rate parity across gender, education, and dependents  

---

## Explainability
- SHAP (SHapley Additive Explanations):
  - Global feature importance (summary plots).
  - Local explanations for individual predictions.
- LIME (Local Interpretable Model‑agnostic Explanations):
  - Case‑by‑case interpretability for loan decisions.

## Deliverables
- Trained models: stored in `ml/models/`
  - `logistic_regression.pkl`
  - `random_forest.pkl`
  - `xgboost.pkl`
  - `lightgbm.pkl`
  - `calibrated_rf.pkl`
- Explainability outputs: stored in `ml/explainability/`
  - SHAP summary plots
  - LIME case explanations
- Fairness evaluation: stored in `ml/fairness/`
  - Bias reports (gender, education, dependents)

