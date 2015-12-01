#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-04 ‏‎‏‎19:49:33
from __future__ import unicode_literals
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

dicdias = {1: 'Lunes', 2: 'Martes', 3: 'Miercoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sabado', 7: 'Domingo'}
timbres = {1: 'Alarma Hora', 2: 'Alarma Incendio', 3: 'Luces'}


# Create your models here.
class Tiempo(models.Model):
    tiempo_dia = models.IntegerField(verbose_name="Dia")
    tiempo_hora = models.IntegerField(verbose_name="Hora", validators=[MinValueValidator(0), MaxValueValidator(23)])
    tiempo_minuto = models.IntegerField(verbose_name="Minuto", validators=[MinValueValidator(0), MaxValueValidator(59)])
    tiempo_tipo = models.IntegerField(verbose_name="Tipo de Alarma",
                                      validators=[MinValueValidator(0), MaxValueValidator(3)])
    tiempo_status = models.TextField(verbose_name="Estado de la alarma", default="Active", editable=False)

    @property
    def __str__(self):
        global dicdias
        return dicdias[int(self.tiempo_dia)] + " " + str(self.tiempo_hora) + ":" + str(
            self.tiempo_minuto) + " Tipo de timbre: " + str(self.tiempo_tipo)

    def get_dia(self):
        global dicdias
        return dicdias[int(self.tiempo_dia)]

    def get_hora(self):
        return self.tiempo_hora

    def get_minuto(self):
        return self.tiempo_minuto

    def get_timbre(self):
        global timbres
        return timbres[int(self.tiempo_tipo)]

    def get_estado(self):
        return self.tiempo_status


class DjkombuMessage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    visible = models.BooleanField()
    sent_at = models.DateTimeField(blank=True, null=True)
    payload = models.TextField()
    queue = models.ForeignKey('DjkombuQueue')

    class Meta:
        managed = False
        db_table = 'djkombu_message'


class DjkombuQueue(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'djkombu_queue'
