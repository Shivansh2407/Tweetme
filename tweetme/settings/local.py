import os
from .base import PROJECT_ROOT

SECRET_KEY = ')_3sp#ux^9bas4!u*krx*m@f_wwf7*u^t1_ivsl@x$5sew0rp*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['octrixtweetapp.herokuapp.com','127.0.0.1']


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), "static-serve")
