# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0005_eventdnotification_guess'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventanotification',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='eventbnotification',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='eventcnotification',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='eventdnotification',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
