import requests

def call_api():
    """
    Function that calls an API with hardcoded credentials.
    This is a BAD practice as secrets are exposed in the code.
    """
    # Hardcoded secrets - BAD PRACTICE!
    api_url = "https://api.example.com/data"
    api_key = "aJ2pRq7Xz9B4tY6vE8sK3dL5mN1oP0wQ_cF3gH5jI7kZ"
    
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
    print("Making API call with hardcoded secrets...")
    result = call_api()
    print(f"API Response: {result}")

if __name__ == "__main__":
    main()