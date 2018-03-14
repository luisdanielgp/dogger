from .base import *
import os

SECRET_KEY = '#i_h0ugm8st^h50%krrmgt)@k@&k^_3gu#w0z8c9_!2lzkbc(+'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dogger',
        'USER': 'dogger_admin',
        'PASSWORD': 'dogger_admin',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

STATICFILES_DIRS = [os.path.join(os.getcwd(), "static")]
