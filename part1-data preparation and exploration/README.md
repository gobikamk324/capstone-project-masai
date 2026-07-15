# Loan Risk Assessment – Part 1 (Data Preparation & EDA)

## Dataset Source
- Origin:Kaggle – Loan Prediction Dataset  
- Raw file: `loan.csv`  
- The dataset contains applicant details such as income, education, marital status, property area, loan amount, credit history, and loan approval status.

## Data Cleaning
Steps applied to prepare the dataset for modeling:

- Missing values handled:
  - Gender, Married, Dependents, Self_Employed, Loan_Amount_Term, Credit_History → filled with mode (most frequent value).
  - LoanAmount → filled with median.
- Encoding categorical variables:
  - Applied one‑hot encoding (`pd.get_dummies`) to convert categorical features into numeric format.
- Normalization:
  - Standardized numeric features (`ApplicantIncome`, `CoapplicantIncome`, `LoanAmount`) using `StandardScaler`.

## Exploratory Data Analysis (EDA)
Performed structured analysis to understand distributions, correlations, and potential bias:

- Distributions:
  - Applicant income histogram → skewed distribution with high‑income outliers.
  - Loan amount histogram → highlights typical loan sizes.
- Outliers:
  - Boxplot of applicant income → reveals extreme high‑income applicants.
- Correlations:
  - Heatmap of numeric features → shows relationships between income, loan amount, and approval.
- Bias checks:
  - Loan approval rates by gender, education, and property area → checked for demographic disparities.
- Class balance:
  - Count plot of Loan_Status → shows distribution of approved vs rejected loans.

Plots saved in: `eda/plots/`  
Examples include:  
- `income_distribution.png`  
- `loan_approval_property_area.png`
- `applicant_income_boxplot.png`  
- `correlation_heatmap.png`  
- `bias_check_gender.png`  

