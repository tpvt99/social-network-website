# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_remove_infowork_work_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infowork',
            name='time_begin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='infowork',
            name='time_end',
            field=models.DateField(null=True),
        ),
    ]
