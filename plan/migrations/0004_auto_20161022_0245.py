# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20161013_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantmoreinfo',
            name='owner_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participantmoreinfo',
            name='user_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
