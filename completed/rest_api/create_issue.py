#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Creates a new Github Issue from the command line.
'''

TOKEN = 'YOUR_TOKEN_GOES_HERE'
GITHUB_API = 'https://api.github.com'

import requests
import argparse
import json
from urlparse import urljoin


def main():
    #
    # Parse arguments
    #
    parser = argparse.ArgumentParser(description='List Github repositories.')
    parser.add_argument('-o',
        required = True,
        dest = 'owner',
        )
    parser.add_argument('-r',
        required = True,
        dest = 'repo',
        )
    parser.add_argument('-t',
        required = True,
        dest = 'title',
        )
    parser.add_argument('-b',
        dest = 'body',
        )
    parser.add_argument('-m',
        dest = 'milestone',
        type = int,
        )
    parser.add_argument('-l',
        nargs = '+',
        dest = 'labels',
        metavar = 'LABEL',
        )
    args = parser.parse_args()
    #
    # Sanity checks
    #
    url = urljoin(GITHUB_API, 'users/%s' % args.owner)
    res = requests.get(url)
    if res.status_code >= 400:
        print 'ERROR Unknown username: %s' % args.owner
        return
    fragment = 'repos/%s/%s' % (args.owner, args.repo)
    url = urljoin(GITHUB_API, fragment)
    res = requests.get(url)
    if res.status_code >= 400:
        print 'ERROR Unknown repository: %s' % args.repo
        return
    if args.milestone:
        fragment = '/repos/%s/%s/milestones/%s' % (args.owner, args.repo, args.milestone)
        url = urljoin(GITHUB_API, fragment)
        res = requests.get(url)
        if res.status_code >= 400:
            print 'ERROR Unknown milestone: %s' % args.milestone
            return
    if args.labels:
        for label in args.labels:
            fragment = '/repos/%s/%s/labels/%s' % (args.owner, args.repo, label)
            url = urljoin(GITHUB_API, fragment)
            res = requests.get(url)
            if res.status_code >= 400:
                print 'ERROR Unknown label: %s' % label
                return
    #
    # Compose REST request
    #
    fragment = '/repos/%s/%s/issues' % (args.owner, args.repo)
    url = urljoin(GITHUB_API, fragment)
    headers = {
        'Authorization': 'token %s' % TOKEN
        }
    payload = {
        'title': args.title,
        }
    if args.milestone:
        payload['milestone'] = args.milestone
    if args.labels:
        payload['labels'] = args.labels
    res = requests.post(
        url,
        headers = headers,
        data = json.dumps(payload),
        )
    #
    # Parse API response
    #
    if res.status_code >= 400:
        msg = res.json.get('message', 'Unknown Error')
        print 'ERROR: %s' % msg
        return
    num = res.json['number']
    href = res.json['html_url']
    print 'New issue #%s created:  %s' % (num, href)

if __name__ == '__main__':
    main()