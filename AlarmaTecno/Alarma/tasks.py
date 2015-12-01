#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-14 ‏‎14:32:30

from __future__ import absolute_import
from celery import task
import datetime
import os
from time import sleep
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AlarmaTecno.settings")
from Alarma.models import Tiempo, DjkombuMessage
from Alarma.timbre import estado


@task
def base():
    x = datetime.datetime.now()
    dicdias = {'MONDAY': 1, 'TUESDAY': 2, 'WEDNESDAY': 3, 'THURSDAY': 4,
               'FRIDAY': 5, 'SATURDAY': 6, 'SUNDAY': 7}
    anho = x.year
    mes = x.month
    dia = x.day
    fecha = datetime.date(anho, mes, dia)
    diactual = dicdias[fecha.strftime('%A').upper()]
    for tiempo in Tiempo.objects.all().raw(
            "Select * From Alarma_tiempo Where tiempo_dia = %s AND tiempo_status = 'Active' Order by tiempo_hora",
            [diactual]):
        x = datetime.datetime.now()
        if tiempo.tiempo_minuto == 0:
            if tiempo.tiempo_hora == x.hour and 59 == x.minute:
                sleep(60 - x.second)
                estado(tiempo.tiempo_tipo)
        else:
            if tiempo.tiempo_hora == x.hour and tiempo.tiempo_minuto - 1 == x.minute:
                sleep(60 - x.second)
                estado(tiempo.tiempo_tipo)


@task
def eliminar():
    DjkombuMessage.objects.all().delete()
    print "Mensajes eliminados"
