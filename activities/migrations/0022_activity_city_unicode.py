# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0021_auto_20160917_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='city_unicode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
