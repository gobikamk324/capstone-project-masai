# Loan Risk Prediction System

## 📌 Introduction
This project predicts loan approval risk using **machine learning (Logistic Regression)** and provides **plain‑English explanations** using a language model (LLM).  
It helps banks assess whether a loan applicant is **low, medium, or high risk**, based on applicant details such as income, loan amount, credit history, and loan term.

---

## 📌 Data Preparation & Preprocessing
1. **Raw dataset** (`cleaned dataset.csv`) contains 13 columns including Loan_ID, applicant details, and loan status.  
2. **Preprocessing steps**:
   - Dropped `Loan_ID` (not useful for prediction).  
   - Filled missing values with median/mode.  
   - Converted `Loan_Status` (Y/N → 1/0).  
   - One‑hot encoded categorical variables (Gender, Education, Property_Area, etc.).  
   - Scaled numeric features (`ApplicantIncome`, `CoapplicantIncome`, `LoanAmount`).  
3. **Final dataset** (`loan_clean.csv`) has 15 columns.  
4. **Model training**:
   - Logistic Regression trained on `loan_clean.csv`.  
   - Model saved as `loan_model.pkl`.  
**Open a terminal/command prompt**
   download the file and instaall the reuirement and 
   Navigate to the project folder in command prompt

     

