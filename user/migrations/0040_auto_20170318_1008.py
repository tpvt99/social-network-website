# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_auto_20170314_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='background_pic',
            field=models.ImageField(null=True, upload_to=user.models.user_backgroundpic_upload),
        ),
    ]
