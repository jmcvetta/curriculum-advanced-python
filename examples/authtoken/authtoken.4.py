#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Get an OAuth token for the Github API
'''

GITHUB_API = 'https://api.github.com'

VALID_SCOPES = [
    'user', 
    'public_repo', 
    'repo', 
    'repo:status',
    'delete_repo',
    'gist'
    ]


import requests
import getpass
import json
import argparse
from urlparse import urljoin


def main():
    #
    # User Input
    #
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('username', metavar='USERNAME', type=str, 
        help='Github username')
    parser.add_argument('--note', type=str, nargs=1, help='Note')
    parser.add_argument('--scope', dest='scopes', type=str, nargs="+", 
        choices=VALID_SCOPES, help='Scope for this token')
    args = parser.parse_args()
    password = getpass.getpass('Github password: ')
    #
    # Compose Request
    #
    url = urljoin(GITHUB_API, 'authorizations')
    payload = {}
    if args.note:
        payload['note'] = args.note
    if args.scopes:
        payload['scopes'] = args.scopes
    res = requests.post(
        url,
        auth = (args.username, password),
        data = json.dumps(payload),
        )
    #
    # Parse Response
    #
    j = json.loads(res.text)
    if res.status_code >= 400:
        msg = j.get('message', 'UNDEFINED ERROR (no error description from server)')
        print 'ERROR: %s' % msg
        return
    print 'New token: %s' % j['token']
    print 'Url: %s' % j['url']
    print 'Scopes: %s' % ', '.join(j['scopes'])
    print 'Note: %s' % j['note']

if __name__ == '__main__':
    main()