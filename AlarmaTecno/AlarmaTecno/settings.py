#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-04 ‏‎‏‎19:49:33

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
djcelery.setup_loader()
BROKER_URL = 'django://'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CELERY_TIMEZONE = 'America/Guayaquil'
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_RESULT_PERSISTENT = False
CELERY_IGNORE_RESULT = True
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nb812krd_^=9gzv#rpi@xfyjgdiiy*lv_nw46c)754xrxepwe$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'Alarma',
    'kombu.transport.django',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'AlarmaTecno.urls'

WSGI_APPLICATION = 'AlarmaTecno.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
            ],
        },
    },
]


DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')
STATIC_URL = '/static/'
STATIC_ROOT_DEVELOPMENT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = (
    'django.core.context_processors.static',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
