#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Queries the Github API for repositories  belonging to the authenticated user.
'''

API_TOKEN = 'YOUR_TOKEN_GOES_HERE'
GITHUB_API = 'https://api.github.com'
VALID_TYPES = ['all', 'owner', 'public', 'private', 'member']

import requests
import argparse
from urlparse import urljoin

def main():
    #
    # Parse arguments
    #
    parser = argparse.ArgumentParser(description='List Github repositories.')
    parser.add_argument('-t', '--type', 
        nargs = 1,
        dest = 'type',
        default = 'all',
        metavar = 'TYPE',
        choices = VALID_TYPES,
        help = 'What type of repos to list',
        )
    args = parser.parse_args()
    # 
    # Build REST request
    #
    headers = {
        'Authorization': 'token %s' % API_TOKEN
        }
    url = urljoin(GITHUB_API, '/user/repos')
    payload = {
        'type': args.type,
        }
    res = requests.get(url, headers=headers, data=payload)
    #
    # Parse API response
    #
    if res.status_code >= 400:
        msg = res.json.get('message', 'Unknown Error')
        print 'ERROR: %s' % msg
        return
    for repo in res.json:
        name = repo['name']
        desc = repo['description']
        num_issues = repo['open_issues']
        print '%s (%s): %s' % (name, num_issues, desc)
    
    
if __name__ == '__main__':
    main()