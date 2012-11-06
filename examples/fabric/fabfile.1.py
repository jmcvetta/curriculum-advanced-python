# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

from fabric.api import run
from fabric.api import env

env.hosts = [
    'newyork',
    'seattle',
    'localhost',
    ]

def host_type():
    run('uname -s')
    
def diskspace():
    run('df')