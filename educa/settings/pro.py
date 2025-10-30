from .base import *

DEBUG = False

ADMINS = (
    ('Bhavani', 'bhavani@testpress.in'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER' : 'educa',
        'PASSWORD' : 'Bhavani333$',
        'HOST': 'localhost',     # since it’s on your system
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
ROOT_URLCONF = 'educa.urls'
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
