# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20160908_1314'),
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='place',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='street',
            new_name='city_code',
        ),
        migrations.AddField(
            model_name='participantmoreinfo',
            name='time_join',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page.City'),
        ),
    ]
