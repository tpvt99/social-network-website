# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20170102_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='born_place',
        ),
        migrations.RemoveField(
            model_name='info',
            name='country_search',
        ),
        migrations.RemoveField(
            model_name='info',
            name='live_place',
        ),
    ]