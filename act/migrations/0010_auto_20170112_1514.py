# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('act', '0009_auto_20170112_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actposttagfriend',
            name='actpost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='act_actposttagfriend_actpost', to='act.ActPost'),
        ),
    ]
