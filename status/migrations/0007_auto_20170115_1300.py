# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0023_auto_20170115_1203'),
        ('status', '0006_status_actpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='activitypost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityPost'),
        ),
    ]