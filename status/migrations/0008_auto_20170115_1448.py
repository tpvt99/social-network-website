# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0061_auto_20170115_1440'),
        ('status', '0007_auto_20170115_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='activitiespost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.ActivitiesPost'),
        ),
    ]
