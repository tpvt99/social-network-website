# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-30 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0046_activityvote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='rank_icon_description',
            new_name='rank_icon_name',
        ),
    ]
