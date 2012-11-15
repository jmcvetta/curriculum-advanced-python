#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Lab - Average Uptime

Write a script that uses the Fabric library to poll a group of hosts for their
uptimes, and displays their average uptime for the user.
'''

import re
from fabric import tasks
from fabric.api import run
from fabric.api import env
from fabric.api import parallel
from fabric.network import disconnect_all


pattern = re.compile(r'up\s+(?:(\d+) days, \s+)?(\d+):(\d+)')

env.hosts = [
    'newyork',
    'seattle',
    'localhost',
    ]


def uptime():
    res = run('uptime')
    match = pattern.search(res)
    if match:
        if match.group(1):
            days = int(match.group(1))
        else:
            days = 0
        hours = int(match.group(2))
        minutes = int(match.group(3))
        minutes += hours * 60
        minutes += days * 24 * 60
        env['uts'].append(minutes)


def main():
    env['uts'] = []
    tasks.execute(uptime)
    uts_list = env['uts']
    if not uts_list:
        print "ERROR: Could not retrieve any uptime values"
        return 
    avg = sum(uts_list) / float(len(uts_list))
    disconnect_all()
    print '-' * 80
    print 'Average uptime: %s minutes' % avg
    print '-' * 80


if __name__ == '__main__':
    main()
    
