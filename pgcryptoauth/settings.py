# -*- coding: utf-8 -*-
"""Default settings for package (overridable with Django settings)."""

from django.conf import settings

#
# Specify the name of the database connection to use. Default to 'default'
#
PGCRYPTOAUTH_DATABASE = getattr(settings, 'PGCRYPTOAUTH_DATABASE', 'default')
