********************
Using Fabric for SSH
********************

Fabric is a library and command-line tool for streamlining the use of SSH for
application deployment or systems administration tasks.

It provides a basic suite of operations for executing local or remote shell
commands (normally or via sudo) and uploading/downloading files, as well as
auxiliary functionality such as prompting the running user for input, or
aborting execution.


``fab`` Command
===============

Fabric provides a command line utility ``fab``, which reads its configuration
from a file named ``fabfile.py`` in directory from which it is run.  A typical
fabfile contains one or more functions to be executed on a group of remote
hosts.

The following example provides functions to check free disk space and host type,
as well as defining a group of hosts on which to run:

.. literalinclude:: examples/fabric/fabfile.0.py
   :linenos:
   :lines: 4-


Once a task is defined, it may be run on one or more servers, like so:

.. code-block:: console

   (sysadmin)$ fab -H newyork,seattle host_type
   [newyork] run: uname -s
   [newyork] out: Linux
   [seattle] run: uname -s
   [seattle] out: Linux
   
   Done.
   Disconnecting from newyork... done.
   Disconnecting from seattle... done.

Rather than supplying hostnames on the command line, you can also define the
group of hosts on which tasks will be run with ``env.hosts``:

.. literalinclude:: examples/fabric/fabfile.1.py
   :linenos:
   :lines: 4-

Now run ``fab`` without a ``-H`` argument:

.. code-block:: console

   (sysadmin)$ fab host_type
   [newyork] run: uname -s
   [newyork] out: Linux
   [seattle] run: uname -s
   [seattle] out: Linux
   [localhost] run: uname -s
   [localhost] out: Linux
   
   Done.
   Disconnecting from newyork... done.
   Disconnecting from seattle... done.
   Disconnecting from localhost... done.


Task arguments
--------------

It's often useful to pass runtime parameters into your tasks, just as you might
during regular Python programming. Fabric has basic support for this using a
shell-compatible notation: ``<task name>:<arg>,<kwarg>=<value>,...``. It's
contrived, but let's extend the above example to say hello to you personally:
[#f1]_

::

   def hello(name="world"):
      print("Hello %s!" % name)


By default, calling ``fab hello`` will still behave as it did before; but now
we can personalize it:

.. code-block:: console

   (sysadmin)$ fab hello:name=Jeff
   Hello Jeff!
   
   Done.

Those already used to programming in Python might have guessed that this
invocation behaves exactly the same way:


.. code-block:: console

   (sysadmin)$ fab hello:Jeff
   Hello Jeff!
   
   Done.


For the time being, your argument values will always show up in Python as
strings and may require a bit of string manipulation for complex types such
as lists. Future versions may add a typecasting system to make this easier.


Library Usage
=============

In addition to use via the fab tool, Fabric’s components may be imported into
other Python code, providing a Pythonic interface to the SSH protocol suite at a
higher level than that provided by e.g. the ssh library (which Fabric itself
uses.) [#f2]_


Lab -- Average Uptime
=====================

Consider the case where we want to collect average uptime from a group of hosts.
File ``labs/fabric/uptime.py`` will get you started:


.. literalinclude:: labs/fabric/uptime.py
   :linenos:
   :lines: 6-


.. rubric:: Footnotes

.. [#f1] http://docs.fabfile.org/en/1.4.2/tutorial.html#task-arguments
.. [#f2] http://stackoverflow.com/a/8166050