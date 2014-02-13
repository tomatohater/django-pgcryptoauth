django-pgcryptoauth
===================

Django hasher for PostgreSQL pgcrypto encoded passwords.

.. image:: https://travis-ci.org/tomatohater/django-pgcryptoauth.png?branch=master
    :target: https://travis-ci.org/tomatohater/django-pgcryptoauth

.. image:: https://coveralls.io/repos/tomatohater/django-pgcryptoauth/badge.png?branch=master
	:target: https://coveralls.io/r/tomatohater/django-pgcryptoauth?branch=master

.. image:: https://badge.fury.io/py/django-pgcryptoauth.png
    :target: http://badge.fury.io/py/django-pgcryptoauth

``django-pgcryptoauth`` is a custom Django password hasher which is intended to provide authentication continuity for legacy passwords that were encrypted with the Postgres pgcrypto extension.

Since we don't have access to the cleartext passwords, we instead just make Django understand and handle the legacy algorithm. When a user successfully logs in, Django will automatically upgrade the password to the preferred algorithm.


Read The Docs
*************

https://django-pgcryptoauth.readthedocs.org/en/latest/