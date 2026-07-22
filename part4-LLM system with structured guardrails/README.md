# 📘 Part‑4: LLM Integration & Structured Outputs

## 🎯 Objective
Integrate a **Large Language Model (LLM)** to explain loan risk predictions in plain English, while enforcing a **strict JSON output schema** for consistency and reliability.

---

## 🚀 Steps
1. **Choose an LLM API**  
   - Options: OpenAI API, Anthropic Claude API, Google Gemini API, or any HTTP/JSON LLM endpoint.  
   - Get your API key from the provider.

2. **Store the API key securely**  
   - Use a `.env` file (gitignored) to store your key.  
   - Example:
     ```env
     OPENAI_API_KEY=your_api_key_here
     ```

3. **Design the prompt + JSON schema**  
   - Prompt should clearly ask the LLM to explain the ML model output.  
   - Example schema:
     ```json
     {
       "risk_level": "low",
       "probability": 0.0,
       "explanation": "Applicant has strong repayment history and manageable loan amount.",
     }
     ```

4. **Call the API via Python**  
   - Use `requests` or the provider’s SDK.  
   - Parse the JSON response.  
   - Validate against the schema using `pydantic` or `jsonschema`.

5. **Handle malformed outputs**  
   - Retry the API call if the response is invalid.  
   - Log errors for debugging.

6.**this is my output**
<img width="953" height="463" alt="Screenshot 2026-07-22 225837" src="https://github.com/user-attachments/assets/7c57783c-e4b9-4290-97bb-10206c9a269a" />
