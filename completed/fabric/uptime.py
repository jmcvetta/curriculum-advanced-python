#!/usr/bin/env python
'''
Lab - Average Uptime

Write a script that uses the Fabric library to poll a group of hosts for their
uptimes, and displays their average uptime for the user.
'''


from fabric import tasks
from fabric.api import run
from fabric.api import env
from fabric.api import parallel
from fabric.network import disconnect_all

env.hosts = [
    'newyork',
    'seattle',
    'localhost',
    ]

@parallel
def uptime():
    res = run('cat /proc/uptime')
    try:
        seconds = float(res.split(' ')[0])
    except:
        print "Oi vey, bad response from server! "
        print res
        return
    return seconds
        

def main():
    uts_dict = tasks.execute(uptime)
    avg_ut = sum(uts_dict.values()) / len(uts_dict)
    print '-' * 80
    print
    print 'Average Uptime: %s' % avg_ut
    print
    print '-' * 80
    disconnect_all() # Call this when you are done, or get an ugly exception!

if __name__ == '__main__':
    main()
    