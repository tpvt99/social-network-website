# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20161212_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchcity',
            name='city',
        ),
        migrations.RemoveField(
            model_name='searchcity',
            name='user',
        ),
        migrations.AddField(
            model_name='info',
            name='head',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='SearchCity',
        ),
    ]
