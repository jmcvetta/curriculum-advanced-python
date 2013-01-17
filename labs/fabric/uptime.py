#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Lab - Average Uptime

Write a script that uses the Fabric library to poll a group of hosts for their
uptimes, and displays their average uptime for the user.
'''


from fabric import tasks
from fabric.api import run
from fabric.api import env
from fabric.network import disconnect_all
import re

env.hosts = [
    'newyork',
    'seattle',
    'localhost',
    ]

def uptime():
    res = run('uptime')
    #
    # Now, examine the result and extract the average uptime
    #

def main():
    env['uts'] = [] # A list of uptime values
    # Use uts_list to collect uptime values from all your tasks
    tasks.execute(uptime)
    # 
    # Now, calculate average uptime...
    #
    disconnect_all() # Call this when you are done, or get an ugly exception!

if __name__ == '__main__':
    main()
    
