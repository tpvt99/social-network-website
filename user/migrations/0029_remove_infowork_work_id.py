# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_auto_20170106_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infowork',
            name='work_id',
        ),
    ]
