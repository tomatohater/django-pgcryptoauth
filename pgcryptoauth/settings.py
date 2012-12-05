from django.conf import settings

#
# Specify the name of the database connection to use. Default to 'default'
#
PGCRYPTOAUTH_DATABASE = getattr(settings, 'PGCRYPTOAUTH_DATABASE', 'default')