#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-06 ‏‎‏‎15:47:10

import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AlarmaTecno.settings")
from Alarma.models import Tiempo

global dicdias
dicdias = {'MONDAY': 1, 'TUESDAY': 2, 'WEDNESDAY': 3, 'THURSDAY': 4,
           'FRIDAY': 5, 'SATURDAY': 6, 'SUNDAY': 7}


def bases():
    diasctual()
    x = datetime.datetime.now()
    for tiempo in Tiempo.objects.all().raw(
            "Select * From Alarma_tiempo Where tiempo_dia = %s AND tiempo_status = 'Active' Order by tiempo_hora",
            [diactual]):
        if tiempo.tiempo_hora == x.hour and tiempo.tiempo_minuto > x.minute:
            return tiempo
        if tiempo.tiempo_hora > x.hour:
            return tiempo
    return None


def comprobar():
    diasctual()
    if list(Tiempo.objects.all().raw("Select * From Alarma_tiempo Where tiempo_dia = %s AND tiempo_status = 'Active'",
                                     [diactual])):
        return True
    else:
        return False


def allday():
    diasctual()
    tiempo = Tiempo.objects.all().raw(
        "Select * From Alarma_tiempo Where tiempo_dia = %s AND tiempo_status = 'Active' Order by tiempo_hora",
        [diactual])
    return tiempo


def diasctual():
    global dicdias, diactual
    x = datetime.datetime.now()
    anho = x.year
    mes = x.month
    dia = x.day
    fecha = datetime.date(anho, mes, dia)
    diactual = dicdias[fecha.strftime('%A').upper()]
