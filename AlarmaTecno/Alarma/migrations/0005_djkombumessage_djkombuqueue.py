# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alarma', '0004_auto_20151025_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjkombuMessage',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('visible', models.BooleanField()),
                ('sent_at', models.DateTimeField(null=True, blank=True)),
                ('payload', models.TextField()),
            ],
            options={
                'db_table': 'djkombu_message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjkombuQueue',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
            options={
                'db_table': 'djkombu_queue',
                'managed': False,
            },
        ),
    ]
