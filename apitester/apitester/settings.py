"""
Django settings for apitester project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = None

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Set this to e.g. ['127.0.0.1', 'localhost'] if DEBUG = False
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'base',
    'obp',
    'runtests',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apitester.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.context_processors.api_root',
                'base.context_processors.api_username',
            ],
        },
    },
]

WSGI_APPLICATION = 'apitester.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbname',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# Set this to your local directory for static files
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static-collected')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
         },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'obp': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    },
}

# Setup a simple cache to avoid hitting the API too often
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
CACHE_TIMEOUT = 10


LOGIN_URL = reverse_lazy('home')


API_DATETIMEFORMAT = '%Y-%m-%dT%H:%M:%SZ'
API_DATEFORMAT = '%Y-%m-%d'


OAUTH_TOKEN_PATH = '/oauth/initiate'
OAUTH_AUTHORIZATION_PATH = '/oauth/authorize'
OAUTH_ACCESS_TOKEN_PATH = '/oauth/token'

DIRECTLOGIN_PATH = '/my/logins/direct'

# Set to true if the API is connected to a core banking system
GATEWAYLOGIN_HAS_CBS = False

API_HOST = 'http://127.0.0.1:8080'
#API_HOST = 'https://apisandbox.openbankproject.com'
API_BASE_PATH = '/obp/v'
API_VERSION = '3.0.0'

REDIRECT_URL='http://127.0.0.1:9090'

# Always save session
SESSION_SAVE_EVERY_REQUEST = True

# Set OAuth client key/secret in apitester/local_settings.py
OAUTH_CONSUMER_KEY = None
OAUTH_CONSUMER_SECRET = None

# Local settings can override anything in here
try:
    from apitester.local_settings import *  # noqa
except ImportError:
    pass

if not OAUTH_CONSUMER_KEY:
    raise ImproperlyConfigured('Missing settings for OAUTH_CONSUMER_KEY')
if not OAUTH_CONSUMER_SECRET:
    raise ImproperlyConfigured('Missing settings for OAUTH_CONSUMER_SECRET')

# Settings here might use parts overwritten in local settings
API_ROOT = API_HOST + API_BASE_PATH + API_VERSION

''' 
REDIRECT_URL should be the url of this appliation. It is used by API_HOST
as the return url. API_HOST is the hostname & scheme of the Open Bank API.
When API Tester (this application) tries to authenticate with Open Bank API
during oauth1 flow, it sends the REDIRECT_URL along with it which is 
used as the redirect url back to this application.
'''
#REDIRECT_URL='https://api-tester.example.com'
