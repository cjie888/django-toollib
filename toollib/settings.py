#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Django settings for toollib project.
#email config
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
EMAIL_HOST = "mail.funshion.com"
EMAIL_HOST_PASSWORD = "funshion"
EMAIL_HOST_USER = "funshion.alert"
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = u"[kuaitu]"
EMAIL_USE_TLS = False
EMAIL_FROM = "funshion.alert@funshion.com"
