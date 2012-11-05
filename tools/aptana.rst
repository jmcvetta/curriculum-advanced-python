*************
Aptana Studio
*************

`Aptana Studio`_ is an IDE - `integrated development environment`_ - based on
the `Eclipse framework`_.  It provides powerful tools for exploring,
understanding, and refactoring your code.

Because Aptana Studio is Eclipse + a plugin, in class I may refer to "Aptana"
and "Eclipse" interchangeably.  Unless explicitly noted, both terms refer to the
combination of Eclipse framework + Aptana Studio plugin.

Aptana's Python support was formerly a separate Eclipse plugin called *PyDev*. 
PyDev was purchased by Aptana and folded into Aptana Studio. Aptana can be
installed as a seperate download, or as an Eclipse plugin.  For convenience we
will download the whole application.

   http://aptana.com/products/studio3/download

.. _integrated development environment: http://en.wikipedia.org/wiki/Integrated_development_environment
.. _Aptana Studio: http://aptana.com/
.. _Eclipse framework: http://eclipse.org


Harmless ``libjpeg`` Error
==========================

The first time you start Apatana Studio, you will get a frightening-looking
error message, complaining that libjpeg.62.so is missing.  This error is
actually quite harmless - it is caused by Aptana trying to display it's one-time
splash screen after a new install.  To display the splash screen requires a JPEG
graphic handling library that we have not installed.  

This bug can be avoided entirely by installing ``libjpeg62``:

.. code-block:: console

   $ sudo apt-get install libjpeg62

However this is not strictly necessary, as the bug does not damage anything, and
appears only the first time a new Apatana installation is run.

Installing Eclipse Plugins
==========================

Each Eclipse plugin has an *Update Site* URL, from which it can be installed.

To install a plugin in Eclipse, choose ``Install New Software...`` from the
``Help`` menu.  Click the ``Add...`` button to add a new plugin repository.  Put
the plugin's *Update Site* URL in the ``Location:`` field.

Once you have added the plugin repository, check the box of the plugin you want
to install.  Click ``Next >``, then click thru until it is installed.  Normally
Eclipse will want to restart itself after a new plugin has been installed.


Vwrapper
--------

Vrapper is an Eclipse plugin providing VI-keys support.  Only install this
plugin if you are *certain* you want it.

Update site:

   ``http://vrapper.sourceforge.net/update-site/stable``


Python Perspective
==================

.. todo:: 

   Describe what perspectives are, and how to select Python perspective,
   including screenshots.

   
Working with Virtual Environments
=================================

Unfortunately, Aptana is not aware of virtual environments by default.  This can
be worked around by manually configuring Aptana to use the Python interpreter
from the virtual environment.  We will configure the interpreter in the course
of starting a new project below.


Starting a New Project
======================

.. todo:: 

   Describe how to start a new project, including screenshots.