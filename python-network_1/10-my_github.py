#!/usr/bin/python3
"""This module or script
takes your GitHub credentials (username and personal access token)
and uses the GitHub API to display your id.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <access_token>".format(sys.argv[0]))
        sys.exit(1)

    username = 'cysron-b'
    access_token = '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'
    url = 'https://api.github.com/user'

    try:
        response = requests.get(url, auth=(username, access_token))
        if response.status_code == 200:
            data = response.json()
            print(data['id'])
        else:
            print(None)
    except ValueError:
        print(None)
