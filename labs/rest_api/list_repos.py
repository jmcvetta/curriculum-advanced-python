#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Lab - List Repositories

Write a script that queries the Github API for repositories 
belonging to the authenticated user.

For each repo, print out its name, its description, and the number
of open issues.
'''

API_TOKEN = 'YOUR_TOKEN_GOES_HERE'
VALID_TYPES = ['all', 'owner', 'public', 'private', 'member']

import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description='List Github repositories.')
    parser.add_argument('-t', '--type', 
        nargs = 1,
        dest = 'type',
        default = 'all',
        metavar = 'TYPE',
        choices = VALID_TYPES,
        help = 'What type of repos to list',
        )
    args = parser.parse_args() # You can access the 'type' argument as args.type
    #
    # Use the authentication token we generated in the previous example
    #
    headers = {
        'Authorization': 'token %s' % API_TOKEN
        }
    #
    # Now, build a REST request, and parse the server's response...
    #
    
    
if __name__ == '__main__':
    main()