#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Django settings for toollib project.
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'd:/sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
     os.path.join(SETTINGS_PATH, 'templates'),
)
SECRET_KEY = '8l&amp;)jd(qf-7u==4lt4lz8emk8+2(8+5x4a$xu7g7ijgn#=p$ma'

#email config
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
EMAIL_HOST = "mail.funshion.com"
EMAIL_HOST_PASSWORD = "funshion"
EMAIL_HOST_USER = "funshion.alert"
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = u"[kuaitu]"
EMAIL_USE_TLS = False
EMAIL_FROM = "funshion.alert@funshion.com"
