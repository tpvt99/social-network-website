# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0010_auto_20160909_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='share',
            field=models.CharField(choices=[('fr', 'friend'), ('frfr', 'friendoffriend'), ('world', 'world')], max_length=10, null=True),
        ),
    ]
