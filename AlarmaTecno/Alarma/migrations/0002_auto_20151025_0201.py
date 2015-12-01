# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alarma', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiempo',
            old_name='tiempo_status',
            new_name='tiempo_statu',
        ),
    ]
