from settings import *
DEBUG = False
ALLOWED_HOSTS = ['www.wilmademunnik.nl']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wilmademunnik_prod',
        'USER': '****',
        'PASSWORD': '****',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'www.wilmademuunik.nl',
    }
}

CONTACT_EMAIL = 'info@wilmademunnik.nl'
