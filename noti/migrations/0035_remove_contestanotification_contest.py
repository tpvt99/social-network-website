# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-15 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0034_contestanotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestanotification',
            name='contest',
        ),
    ]
