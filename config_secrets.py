import requests
import config

def call_api():
    """
    Function that calls an API with credentials from a config file.
    This is BETTER than hardcoding, but the config file still contains plaintext secrets.
    The config file should be added to .gitignore to prevent it from being committed.
    """
    # Get secrets from config file
    api_url = config.API_URL
    api_key = config.API_KEY
    
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
    print("Making API call with secrets from config file...")
    result = call_api()
    print(f"API Response: {result}")

if __name__ == "__main__":
    main()