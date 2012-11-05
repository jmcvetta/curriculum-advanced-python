***************
Python Packages
***************

Earlier we installed packages system-wide using the Ubuntu package manager,
``apt-get``.  Now we will install some Python packages locally, into our 
virtual environment.  We will use Pip, the Python package manager.  Pip is aware
of virtual environments.  If you have a virtual environment active when you call Pip,
the requested packages will be installed into the active virtual environmentment.  


Package Descriptions
====================

The following packages are required to complete this course:

==========================   =======================================================
Package                      Description
==========================   =======================================================
django                       Web application framework
fabric                       SSH library and command line tool
ipython                      Interactive Python shell
psycopg2                     PostgreSQL driver
requests                     HTTP for humans
==========================   =======================================================




Installation
============

Use ``pip install`` to install the required packages, as well as their dependencies:

.. code-block:: console

   (class)$ sudo pip install \
   django \
   fabric \
   ipython \
   psycopg2 \
   requests \