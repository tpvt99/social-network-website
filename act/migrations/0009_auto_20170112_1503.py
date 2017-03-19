# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('act', '0008_actpostcomment_actposttagfriend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actposttagfriend',
            name='act',
        ),
        migrations.AddField(
            model_name='actposttagfriend',
            name='actpost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='act_actposttagfriend_actpost', to='act.Act'),
        ),
    ]
