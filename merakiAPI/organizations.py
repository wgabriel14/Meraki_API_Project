"""
***** ORGANIZATIONS.PY *****
List all the organizations you have access to with the API Key
"""


import requests
import pprint as pp
import json


def list_organizations():
    url = "https://api.meraki.com/api/v1/organizations"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    pp.pprint(response.json())


if __name__ == "__main__":
    list_organizations()