# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-14 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventspost',
            name='image',
            field=models.ImageField(null=True, upload_to=events.models.eventspost_image_upload),
        ),
    ]