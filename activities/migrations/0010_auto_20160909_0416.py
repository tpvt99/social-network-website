# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 04:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0009_activity_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='image',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='is_hour',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='is_share',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='title',
        ),
    ]