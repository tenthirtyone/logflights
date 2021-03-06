"""
Django settings for logflights project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import json
import git
import socket
from google.auth import default as googleDefaultCredentials
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hsq&m-4^c-7i)k(=(6k!ri+j00i$n=$n&l6!xh(9!+e*91&+2h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOGFLIGHTS_ENVIRONMENT = 'dev'
LOGFLIGHTS_DOMAIN = socket.gethostname()
DEPLOYMENT_ID = None

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'planner',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'storages',
    'widget_tweaks',
    'planner.custom_tag',
    'pyulog',
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.contrib.celery'
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

ROOT_URLCONF = 'logflights.urls'

STRINGS = 'logflights.strings'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export'
            ],
        },
    },
]

WSGI_APPLICATION = 'logflights.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Terms of service / privacy policy relative to static directory
TERMS_TOS = 'planner/md/terms.md'
TERMS_PRIVACY = 'planner/md/privacy.md'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# set your own google analytics key
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-XXXXXXXXX-1'

SETTINGS_EXPORT = [
    'GOOGLE_ANALYTICS_PROPERTY_ID'
]

#celery configurations
CELERY_BROKER_URL = 'redis://localhost:6379/'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/'
CELERY_ACCEPT_CONTENT = ['pickle']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'Etc/UTC'


# import local settings

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = "none"

ACCOUNT_SIGNUP_FORM_CLASS = "planner.forms.SignupForm"
LOGIN_REDIRECT_URL = "/planner/vehicle/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login/"
LOGIN_URL = "/accounts/login/"

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_CREDENTIALS = None
GS_BUCKET_NAME = os.getenv("GS_BUCKET_NAME", "logflights_data_test")

GIT_REVISION = None
try:
    repo = git.Repo(search_parent_directories=True)
    GIT_REVISION = repo.head.object.hexsha[0:7]
except:
    pass

# import local settings
try:
    from local_settings import *
except Exception as e:
    pass

# Set up environments post local settings import
# Continuous integration settings for unit/functional tests
if LOGFLIGHTS_ENVIRONMENT == 'ci':
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
# All other environments should be fully operational
else:
    try:
        if GS_CREDENTIALS is None:
            GS_CREDENTIALS, project = googleDefaultCredentials()
    except Exception as e:
        raise ImproperlyConfigured(
            "Google Credentials must be available for import.\n" +
            "Error: " + str(e)
            )
