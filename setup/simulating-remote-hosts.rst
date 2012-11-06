.. highlight:: console

***********************
Simulating Remote Hosts
***********************


Some of the class examples involve communicating with remote unix servers. 
Since the class will not necessarily have access to real remote servers, we will
use ``/etc/hosts`` to simulate remote servers using only our local system.

Earlier we installed package ``openssh-server``, the OpenSSH secure shell
server.  This will allow us to login to our VMs using SSH.


``/etc/hosts``
==============

When a unix system attempts to resolve a domain name into an IP address, it first looks in
the file ``/etc/hosts``.  If an entry is found, the name is resolved to that
address.  Otherwise, the system then queries a DNS server.

We will add two entries, named ``newyork`` and ``seattle`` to our ``/etc/hosts``
file, pointing those names to 127.0.0.1, the loopback IP address.  (I.e.
pointing them back at our local host.)

Initially your ``/etc/hosts`` file should look something like this:

::

   127.0.0.1   localhost
   127.0.1.1   sbtrain-vbox
   
   # The following lines are desirable for IPv6 capable hosts
   ::1     ip6-localhost ip6-loopback
   fe00::0 ip6-localnet
   ff00::0 ip6-mcastprefix
   ff02::1 ip6-allnodes
   ff02::2 ip6-allrouters

   
Modify it to look like this:

::

   127.0.0.1   localhost
   127.0.0.1   newyork
   127.0.0.1   seattle
   127.0.1.1   sbtrain-vbox
   
   # The following lines are desirable for IPv6 capable hosts
   ::1     ip6-localhost ip6-loopback
   fe00::0 ip6-localnet
   ff00::0 ip6-mcastprefix
   ff02::1 ip6-allnodes
   ff02::2 ip6-allrouters


SSH Key Setup
=============

We will now configure our VM's SSH keys, so we can login without typing our credentials.


Generate a Key Pair
-------------------

Generate a new public/private SSH keypair::

   student@sbtrain-vbox:~$ ssh-keygen 
   Generating public/private rsa key pair.
   Enter file in which to save the key (/home/student/.ssh/id_rsa): 
   Created directory '/home/student/.ssh'.
   Enter passphrase (empty for no passphrase): 
   Enter same passphrase again: 
   Your identification has been saved in /home/student/.ssh/id_rsa.
   Your public key has been saved in /home/student/.ssh/id_rsa.pub.
   The key fingerprint is:
   38:a2:64:4a:9b:25:17:36:67:4b:a0:4a:42:ae:0e:90 student@sbtrain-vbox
   The key's randomart image is:
   +--[ RSA 2048]----+
   | . .             |
   |o.. .            |
   |E+ + +           |
   |* . * ..         |
   |+ooo..o S        |
   |++*. . .         |
   |.+.              |
   |                 |
   |                 |
   +-----------------+
   student@sbtrain-vbox:~/.ssh$ ls
   id_rsa  id_rsa.pub
   

Authorized Keys
---------------

Create an ``authorized_keys`` file containing the newly created public key::

   student@sbtrain-vbox:~/.ssh$ cat id_rsa.pub >> authorized_keys


Verify Key Fingerprints
-----------------------

For each of our simulated hosts, we will need to verify the SSH key fingerprint
one time before we can do fully automated logins::

   student@sbtrain-vbox:~/.ssh$ ssh seattle
   The authenticity of host 'seattle (127.0.0.1)' can't be established.
   ECDSA key fingerprint is f3:c7:4b:87:c2:31:6d:ef:44:45:85:9a:21:e6:3c:7b.
   Are you sure you want to continue connecting (yes/no)? yes
   Warning: Permanently added 'seattle' (ECDSA) to the list of known hosts.
   Welcome to Ubuntu 12.04.1 LTS (GNU/Linux 3.2.0-29-generic-pae i686)
   
    * Documentation:  https://help.ubuntu.com/
   
   
   The programs included with the Ubuntu system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.
   
   Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
   applicable law.
   
   student@sbtrain-vbox:~$ exit
   logout
   Connection to seattle closed.
   student@sbtrain-vbox:~/.ssh$ 

Repeat the same command for ``newyork`` and ``localhost``.
   
   
Automatic Login
===============

If you have completed all steps above successfully, you should now be able to
login to any of our "remote" hosts without any keyboard interaction::

   student@sbtrain-vbox:~/.ssh$ ssh seattle
   Welcome to Ubuntu 12.04.1 LTS (GNU/Linux 3.2.0-29-generic-pae i686)
   
    * Documentation:  https://help.ubuntu.com/
   
   Last login: Mon Nov  5 16:50:03 2012 from localhost
   student@sbtrain-vbox:~$ exit
   logout
   Connection to seattle closed.
   student@sbtrain-vbox:~/.ssh$ 
   
   
   
   
   
