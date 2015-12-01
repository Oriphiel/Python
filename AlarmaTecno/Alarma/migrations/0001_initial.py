# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tiempo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiempo_dia', models.IntegerField(verbose_name=b'Dia')),
                ('tiempo_hora', models.IntegerField(verbose_name=b'Hora', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)])),
                ('tiempo_minuto', models.IntegerField(verbose_name=b'Minuto', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)])),
                ('tiempo_tipo', models.IntegerField(verbose_name=b'Tipo de Alarma', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('tiempo_status', models.TextField(default=b'Active', verbose_name=b'Estado de la alarma')),
            ],
        ),
    ]
