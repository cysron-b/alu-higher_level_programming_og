#!/usr/bin/python3
"""A script that takes GitHub credentials."""


if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    url = 'https://api.github.com/user'
    user = "cysron-b"
    xyz = "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"
    authori = HTTPBasicAuth(username=user, password=xyz)
    response = requests.get(url, auth=authori)
    result = response.json()
    print(result.get('id'))
