#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Get an OAuth token for the Github API
'''

GITHUB_API = 'https://api.github.com'


import requests
import json
from urlparse import urljoin


def main():
    #
    # User Input
    #
    username = raw_input('Github username: ')
    password = raw_input('Github password: ')
    #
    # Compose Request
    #
    url = urljoin(GITHUB_API, 'authorizations')
    payload = {}
    res = requests.post(
        url,
        auth = (username, password),
        data = json.dumps(payload),
        )
    print res.text

if __name__ == '__main__':
    main()