# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 16:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_activityenjoy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activityenjoy',
            old_name='paricipants',
            new_name='participants',
        ),
    ]
