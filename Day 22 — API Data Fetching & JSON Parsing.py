import requests
import pandas as pd
import time

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Maximum number of attempts
max_retries = 3

for attempt in range(1, max_retries + 1):

    try:
        print(f"\nAttempt {attempt}...")

        # Send GET request
        response = requests.get(url, timeout=10)

        # Check status code
        if response.status_code == 200:

            print("Request successful!")
            print("Status Code:", response.status_code)

            # Convert JSON response into Python data
            data = response.json()

            print("\nJSON data received successfully.")

            # Convert data into Pandas DataFrame
            df = pd.DataFrame(data)

            print("\nPandas DataFrame:")
            print(df)

            break

        else:
            print("Request failed!")
            print("Status Code:", response.status_code)

    except requests.exceptions.RequestException as e:

        print("Network error:", e)

    # Retry if request was unsuccessful
    if attempt < max_retries:
        print("Retrying in 2 seconds...")
        time.sleep(2)

else:
    print("\nAPI request failed after all retry attempts.")