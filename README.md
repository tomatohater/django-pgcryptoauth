django-pgcryptoauth
===================

Django hasher for pgcrypto encoded passwords.

``django-pgcryptoauth`` is a custom Django password hasher which is intended to provide authentication continuity for legacy passwords that were encrypted with the Postgres pgcrypto extension.

Since we don't have access to the cleartext passwords, we instead just make Django understand and handle the legacy algorithm. When a user successfully logs in, Django will automatically upgrade the password to the preferred algorithm.


Dependencies
------------

Of course, you will need to be using a PostgreSQL database with the [pgcrypto](http://www.postgresql.org/docs/9.1/static/pgcrypto.html) extension installed.


Installation
------------

1. Install the ``django-pgcryptoauth`` package:

        pip install -e git+git@github.com:tomatohater/django-pgcryptoauth.git@master#egg=django-pgcryptoauth


2. Add ``pgcryptoauth`` to your ``INSTALLED_APPS``:

        INSTALLED_APPS = (
            ...
            'pgcryptoauth',
            ...
        )

3. Add ``pgcryptoauth.hashers.PgCryptoPasswordHasher`` to PASSWORD_HASHERS in your Django settings:

        PASSWORD_HASHERS = (
            ...
            'pgcryptoauth.hashers.PgCryptoPasswordHasher',
        )

Note: This hasher should probably at the bottom of the list so that other hashers take priority. See https://docs.djangoproject.com/en/1.4/topics/auth/#how-django-stores-passwords


Loading legacy data
-------------------

Note, the legacy pgcrypto hashed passwords look like ``$1$BFw5nhna$XeiE8c4FInYGp3oND2l9n1``. When migrating these legacy passwords, we simply need to prefix the hash with the ``pgcrypto$`` algorithm:

    user.password = 'pgcrypto$$1$BFw5nhna$XeiE8c4FInYGp3oND2l9n1'
    user.save()

If you review that users password via the Django ``auth.user`` admin, you should see:

    algorithm: pgcrypto
    hash: $1$BFw******************************************