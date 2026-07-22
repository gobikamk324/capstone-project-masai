import os
import warnings
import logging
import joblib
import numpy as np
import pandas as pd
from transformers import pipeline
from tenacity import retry, stop_after_attempt, wait_fixed

warnings.filterwarnings("ignore", category=UserWarning)

logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_request(text):
    logging.info(f"Request: {text}")

def log_response(text):
    logging.info(f"Response: {text}")

def log_error(error):
    logging.error(f"Error: {error}")

def validate_user_input(text: str):
    if not text or len(text.strip()) == 0:
        raise ValueError("Empty input is not allowed.")
    if len(text) > 1000:
        raise ValueError("Input too long.")
    return text.strip()

# Load your trained model
model = joblib.load("loan_model.pkl")

def run_loan_risk_model():
    # Load cleaned encoded dataset (15 columns)
    df = pd.read_csv("loan_clean.csv")

    # Extract feature columns (exclude target)
    feature_cols = df.drop("Loan_Status", axis=1).columns

    # Create empty input row
    X_input = pd.DataFrame(columns=feature_cols)
    X_input.loc[0] = 0  # initialize with zeros

    print("\n--- Enter Loan Details ---")
    income = float(input("Monthly Income: "))
    loan_amt = float(input("Loan Amount: "))
    credit = float(input("Credit History (0 or 1): "))
    term = float(input("Loan Term (in days): "))

    # Fill numeric values
    X_input["ApplicantIncome"] = income
    X_input["LoanAmount"] = loan_amt
    X_input["Credit_History"] = credit
    X_input["Loan_Amount_Term"] = term

    # Scale numeric values using same scaler used in training
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    num_cols = ['ApplicantIncome','CoapplicantIncome','LoanAmount']
    scaler.fit(df[num_cols])
    X_input[num_cols] = scaler.transform(X_input[num_cols])

    # Predict probability
    prob = model.predict_proba(X_input)[0][1]

    if prob > 0.7:
        risk = "high"
    elif prob > 0.4:
        risk = "medium"
    else:
        risk = "low"

    ml_output = {
        "risk": risk,
        "probability": round(prob, 2),
        "features_triggered": ["user_input_processed"]
    }

    print("\nML Model Output:", ml_output)
    return ml_output

def build_llm_prompt(ml_output: dict, user_sentence: str) -> str:
    return (
        f"The loan risk model predicted a {ml_output['risk']} risk "
        f"with probability {ml_output['probability']}. "
        f"The user also said: \"{user_sentence}\". "
        "Explain in plain English why the risk is this level, "
        "what it means for the applicant, and what actions the bank should take."
    )


token = os.getenv("HF_TOKEN")

generator = pipeline("text-generation", model="gpt2", token=token)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def generate_text_safe(prompt: str):
    return generator(
        prompt,
        max_new_tokens=120,
        clean_up_tokenization_spaces=False
    )

def main():
    try:
        ml_output = run_loan_risk_model()

        # Let the user add their own sentence
        user_sentence = input("\nEnter your own sentence to include in the explanation: ")

        prompt = build_llm_prompt(ml_output, user_sentence)

        validated_prompt = validate_user_input(prompt)
        log_request(validated_prompt)

        result = generate_text_safe(validated_prompt)
        llm_text = result[0]["generated_text"]

        log_response(llm_text)

        print("\n=== FINAL EXPLANATION ===")
        print(llm_text)

    except Exception as e:
        log_error(e)
        print("System failed:", e)


if __name__ == "__main__":
    main()
