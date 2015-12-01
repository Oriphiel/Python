# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alarma', '0003_auto_20151025_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo',
            name='tiempo_status',
            field=models.TextField(default=b'Active', verbose_name=b'Estado de la alarma', editable=False),
        ),
    ]
