***************
System Packages
***************

Since we are starting with a fresh install of Ubuntu 12.04, we need to install
various useful libraries and applications.  Ubuntu, like most Linux systems,
uses a `package manager`_ to control installation of software packages.  The
Ubuntu package manager is called ``apt-get``.

.. _package manager: http://en.wikipedia.org/wiki/Package_management_system


Package Descriptions
====================

The following packages are required to complete this course:

==============================    ==============================================
Package                           Description
==============================    ==============================================
openjdk-7-jdk                     Java Development Kit
openssh-server                    SSH server
postgresql-9.1                    Database Server
postgresql-server-dev-9.1         Development headers for PostgreSQL
python-pip                        Python package manager 
python-virtualenv                 Python virtual environment support
python2.7-dev                     Python development headers
virtualenvwrapper                 Tool for convenient virtual environment usage
==============================    ==============================================



Installation
============

Use ``apt-get install`` to install the required packages, as well as their dependencies:

.. code-block:: console

   $ sudo apt-get install \
   openjdk-7-jdk \
   openssh-server \
   postgresql-9.1 \
   postgresql-server-dev-9.1 \
   python-pip \
   python-virtualenv \
   python2.7-dev \
   virtualenvwrapper