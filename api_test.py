import os
import requests
import logging
from dotenv import load_dotenv

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")

# Define headers and payload for chat/completions
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
    "x-ms-model-mesh-model-name": "Mistral-Small"  # Updated to Mistral-Small
}
payload = {
    "messages": [
        {"role": "system", "content": "You are a legal assistant that analyzes contract clauses."},
        {"role": "user", "content": "Analyze this legal clause: The tenant shall be responsible for repairs during the lease term."}
    ]
}

# Log the request details
logging.debug(f"Request URL: {ENDPOINT}")
logging.debug(f"Headers: {headers}")
logging.debug(f"Payload: {payload}")

# Make the API request
try:
    response = requests.post(
        ENDPOINT,  # Use ENDPOINT directly without appending anything
        headers=headers,
        json=payload
    )

    # Log the response details
    logging.debug(f"Response Status Code: {response.status_code}")
    logging.debug(f"Response Content: {response.text}")

    # Display the response
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)

except Exception as e:
    logging.error(f"An exception occurred: {e}")
