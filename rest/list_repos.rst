*******************************
Lab -- List Github Repositories
*******************************

Let's suppose we want to list all the Github repositories associated with the
authenticated user.  

Github defines several types of repository that can be listed:

* ``all``
* ``owner``
* ``public``
* ``private``
* ``member``

Our application should query for ``all`` by default, but allow the user to
specify a different type.

Argparse
========

A production quality command line utility will typically require the ability to
accept arguments when it is called.  While it is *possible* to parse these
arguments manually from ``sys.argv``, the recommended technique is to use the
``argparse`` library.  Argparse is part of the Python standard library, and is
`very well documented`_.

Note:  Argparse was introduced in Python 2.7.  Prior versions of Python include
an earlier library, ``optparse``.  Argparse is intended as a full replacement
for optparse, and so usage of the latter is deprecated.

.. _very well documented: http://docs.python.org/dev/library/argparse.html


Lab
===

File ``labs/rest_api/list_repos.py`` will get you started:

.. literalinclude:: ../labs/rest_api/list_repos.py
   :linenos:
   :lines: 6-