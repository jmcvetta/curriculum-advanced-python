******************************
Generate a Github OAuth2 Token
******************************

There are two ways to authenticate with the GitHub API: HTTP basic auth, and
OAuth2. [#f1]_  It is preferable to use OAuth2, so your script can run without
user input, and without storing your password.

The OAauth2 token can be sent in the request header, or as a parameter.  We will
send it as a header in later examples.




POST Request
============

First, we will prompt the user for username/password, and compose a POST request
to the API.  The request format is documented in the `OAuth section`_ of the
Github API docs.

.. _Oauth Section: http://developer.github.com/v3/oauth/#create-a-new-authorization

.. literalinclude:: ../examples/authtoken/authtoken.0.py
   :linenos:
   :lines: 10-

Let's give it a try:

.. code-block:: console

   (class)$ python authtoken.py 
   Github username: jmcvetta
   Github password: fooba    

That's not good - our password is shown when we type it!


Password Privacy
================

We can protect the user's privacy while inputting their password with the
``getpass`` library.  While we're at it, we can prompt the user for an optional
note to describe how this token will be used.


.. literalinclude:: ../examples/authtoken/authtoken.1.py
   :linenos:
   :lines: 10-
   :emphasize-lines: 5,15-16,22-23
   
Let's give it a try:

.. code-block:: console

   (class)$ python authtoken.py 
   Github username: jmcvetta
   Github password: 
   Note (optional): admin script
   {"scopes":[],"note_url":null,"created_at":"2012-10-21T05:32:30Z","url":"https://api.github.com/authorizations/744660","app":{"url":"http://developer.github.com/v3/oauth/#oauth-authorizations-api","name":"admin script (API)"},"updated_at":"2012-10-21T05:32:30Z","token":"a977026974077e83e593744aa9308422e92a26bd","note":"admin script","id":744660}
   
Seems to have worked!  The response is a big JSON blob.


JSON Parsing
============

We can parse the JSON response and provide just the token, in nice
human-readable form, to the user.  

Explore the response data by setting a breakpoint and running our program in the
debugger.  Start by parsing ``res.text`` into JSON, and examining the keys.

The token lives in the creatively-named field ``token``.  We will extract it and
print it for the user.

.. literalinclude:: ../examples/authtoken/authtoken.2.py
   :linenos:
   :lines: 10-
   :emphasize-lines: 32-34


Let's give it a try:

.. code-block:: console

   (class)$ python authtoken.py 
   Github username: jmcvetta
   Github password: 
   Note (optional): admin script
   New token: 9c0e2ab295ee0e92130142ad3c90bbf5fe93642f


Bingo - it worked!


Error Handling
==============

But what if we don't type the right username/password combo?

.. code-block:: console

   (class)$ python authtoken.py 
   Github username: jmcvetta
   Github password: 
   Note (optional): 
   Traceback (most recent call last):
     File "authtoken.2.py", line 46, in <module>
       main()
     File "authtoken.2.py", line 42, in main
       token = j['token']
   KeyError: 'token'


Gross.  

Once again we can run our program in the debugger to explore the server's
response.  It looks like we have a ``res.status_code`` of 401.  Any HTTP
response code 400 or above indicates an error.  It also looks like the server
helpfully provides a ``message`` field with an error message.

We can look for response codes >= 400 and present the user a friendly error
message:

.. literalinclude:: ../examples/authtoken/authtoken.3.py
   :linenos:
   :lines: 10-
   :emphasize-lines: 33-36

Let's give it a try:

.. code-block:: console

   (class)$ python authtoken.py 
   Github username: jmcvetta
   Github password: 
   Note (optional): 
   ERROR: Bad credentials

Now we have a friendly, useful program.



.. rubric:: Footnotes

.. [#f1] http://developer.github.com/v3/#authentication