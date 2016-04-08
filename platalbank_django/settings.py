"""
Django settings for platalbank_django project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#AUTH_USER_MODEL = 'platalbank_auth.User'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

if DEBUG:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'lhmb7%#jcltxzjo%pl(pay_8t69z^)mci4oppn#a(#6%=9vli8'

    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    # SECURITY WARNING: keep the secret key used in production secret!
    with open('secret_key.txt') as f:
            SECRET_KEY = f.read().strip()

    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

    with open("db_password.txt") as f:
        _pass = f.read().strip()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'superette',
            'USER': 'superette',
            'PASSWORD': _pass,
            'HOST': 'localhost',
        }
    }


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
#    'platalbank_auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'platalbank_core',
)

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
        'platalbank_test',
    )

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'platalbank_django.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'platalbank_django.wsgi.application'



#AUTHENTICATION_BACKENDS = (
#    'platalbank_auth.backends.FrankizLDAPBackend',
#    'django.contrib.auth.backends.ModelBackend',
#)
AUTH_LDAP_SERVER_URI = "ldap://frankiz"
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=eleves,dc=frankiz,dc=net"
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' :[
        #'rest_framework.permissions.AllowAny', #TODO
        'rest_framework.permissions.IsAuthenticated',
    ],
    #'DEFAULT_PAGINATION_CLASS': 'platalbank_django.pagination.CustomPagination',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',  # TODO: remove
        'rest_framework.authentication.SessionAuthentication',  # TODO: remove
    ),

    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter'
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/assets/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "assets/static/")

MEDIA_ROOT = os.path.join(BASE_DIR, "assets/media/")

MEDIA_URL = '/assets/media/'

# CORS headers

CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'platalbank_core.User'

DEFAULT_FROM_EMAIL = "superette@binets.polytechnique.fr"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

ADMINS = (("Superette Webmasters", "root+superette@eleves.polytechnique.fr"),)
