#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-04 ‏‎‏‎19:49:33

from django.contrib import admin
from kombu.transport.django import models as kombu_models
from django.contrib.auth.models import Permission
admin.site.register(Permission)
admin.site.register(kombu_models.Message)
