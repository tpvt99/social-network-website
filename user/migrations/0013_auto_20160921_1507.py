# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_activityonpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityonpost',
            name='is_newest',
        ),
        migrations.AddField(
            model_name='activityonpost',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='activityonpost',
            name='activity_icon',
            field=models.CharField(choices=[('Sport', (('1', 'active person'), ('2', 'badminton'), ('3', 'ride bike'), ('4', 'climbing'), ('5', 'go fishing'), ('6', 'golf'), ('7', 'horse riding'), ('8', 'flying a kite'), ('9', 'canoe'), ('10', 'swimming'), ('11', 'camping'), ('12', 'running'), ('13', 'skateboard'), ('14', 'ski-lift'), ('15', 'surfer'), ('16', 'walking')))], max_length=10),
        ),
    ]
