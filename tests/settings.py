SECRET_KEY = 'e1_+kz-6(n*l@9l6-yf7i*k%@n*r&(r+q6be#mw%j)x1f45+++'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'pgcryptoauth',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pgcryptoauth_test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

PASSWORD_HASHERS = ('pgcryptoauth.hashers.PgCryptoPasswordHasher', )
