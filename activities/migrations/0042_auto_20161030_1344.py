# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-30 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0041_moreinfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='vote',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='vote_icon_description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='vote_icon_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='vote_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
