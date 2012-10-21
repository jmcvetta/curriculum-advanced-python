******
Aptana
******

Aptana is a powerful IDE - integrated development environment - based on the
`Eclipse framework`_.  It provides valuable tools for understanding, browsing, and
refactoring your code.

Aptana's Python support was formerly a separate Eclipse plugin called *PyDev*. 
PyDev was purchased by Aptana and folded into Aptana Studio. Aptana can be
installed as a seperate download, or as an Eclipse plugin.  For convenience we
will download the whole application.

   http://aptana.com/products/studio3/download

.. _`Aptana Studio`: http://aptana.com/
.. _Eclipse framework: http://eclipse.org


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

   
Working with Virtual Environments
=================================

.. todo::

   Describe how to configure Apatana to work with virtualenv.
