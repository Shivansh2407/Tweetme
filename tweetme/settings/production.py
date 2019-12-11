import os
import dj_database_url
from .base import PROJECT_ROOT

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =')_3sp#ux^9bas4!u*krx*m@f_wwf7*u^t1_ivsl@x$5sew0rp*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['octrixtweetapp.herokuapp.com','127.0.0.1']


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(conn_max_age=500)
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static-serve')


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# HTTPS

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


# redirect all HTTP traffic to HTTPS

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
