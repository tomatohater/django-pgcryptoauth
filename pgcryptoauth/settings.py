# -*- coding: utf-8 -*-
"""Default settings for package (overridable with Django settings)."""

from django.conf import settings

#
# Specify the name of the database connection to use. Default to 'default'
#
PGCRYPTOAUTH_DATABASE = getattr(settings, 'PGCRYPTOAUTH_DATABASE', 'default')

#
# Encryption algorithm to use. Default to 'md5'.
# For details see: https://www.postgresql.org/docs/current/static/pgcrypto.html#PGCRYPTO-CRYPT-ALGORITHMS
#
PGCRYPTOAUTH_ALGORITHM = getattr(settings, 'PGCRYPTOAUTH_ALGORITHM', 'md5')
