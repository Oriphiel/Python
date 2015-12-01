#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-14 ‏‎‏‎14:24:54

from __future__ import absolute_import
import os
from celery import Celery, platforms
from django.conf import settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AlarmaTecno.settings')

app = Celery('AlarmaTecno')
platforms.C_FORCE_ROOT = True
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
