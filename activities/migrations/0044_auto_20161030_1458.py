# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-30 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0043_auto_20161030_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='vote',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='vote_icon_description',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='vote_icon_number',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='vote_name',
        ),
    ]
