import os
import requests

def call_api():
    """
    Function that calls an API with credentials from environment variables.
    This is a GOOD practice as no secrets are stored in the codebase.
    Environment variables should be set securely in the deployment environment.
    """
    # Get secrets from environment variables
    api_url = os.environ.get("API_URL")
    api_key = os.environ.get("API_KEY")
    
    # Validate that environment variables are set
    if not api_url or not api_key:
        return {"error": "Environment variables API_URL and/or API_KEY are not set"}
    
    # Make API call
    response = requests.get(
        api_url,
        headers={"Authorization": f"Bearer {api_key}"}
    )
    
    # Process response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API call failed with status code: {response.status_code}"}

def main():
    print("Making API call with secrets from environment variables...")
    result = call_api()
    print(f"API Response: {result}")

if __name__ == "__main__":
    main()