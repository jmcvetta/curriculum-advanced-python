#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Lab - Create a new Github Issue from the command line.

Write a script that can create a new Issue on Github, based on the command line
arguments supplied by the user.  Only those arguments required to create the 
Issue should be mandatory, all others optional.

On success, the script should display the issue number and a link to the HTML
page (not the API link) for the Issue.  On error, it should display a friendly,
informative error message.
'''

TOKEN = 'YOUR_TOKEN_GOES_HERE'
GITHUB_API = 'https://api.github.com'


import argparse
import json
import requests
from urlparse import urljoin


def main():
    pass

if __name__ == '__main__':
    main()