import requests
import json

# Set the API endpoint URL
url = "http://localhost:3000"

# Set the request headers
headers = {
    "Accept": "application/json",
}

# Send the GET request
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    # store the JSON response
    json_data = response.json()

    # parsed_json = json.loads(json_data)

    # Print the response data (the OpenAPI specification)
    print(json.dumps(json_data, indent=4, sort_keys=True))
else:
    print(f"Request failed with status code: {response.status_code}")