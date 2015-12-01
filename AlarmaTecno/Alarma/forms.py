#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-05 18:45:40

from django.forms import ModelForm
from Alarma.models import Tiempo


class TiempoForm(ModelForm):
    class Meta:
        model = Tiempo
        fields = '__all__'
