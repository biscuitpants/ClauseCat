import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")

def analyze_clause(text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "input": text
    }
    response = requests.post(f"{ENDPOINT}/analyze", headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

if __name__ == "__main__":
    sample_text = "The tenant shall be responsible for repairs during the lease term."
    result = analyze_clause(sample_text)
    print("Analysis Result:", result)
