django-pgcryptoauth
===================

Django hasher for PostgreSQL pgcrypto encoded passwords.

``django-pgcryptoauth`` is a custom Django password hasher which is intended to provide authentication continuity for legacy passwords that were encrypted with the Postgres pgcrypto extension.

Since we don't have access to the cleartext passwords, we instead just make Django understand and handle the legacy algorithm. When a user successfully logs in, Django will automatically upgrade the password to the preferred algorithm.


Read The Docs
-------------

https://django-pgcryptoauth.readthedocs.org/en/latest/