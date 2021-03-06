# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-30 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0045_auto_20161030_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0)),
                ('vote_name', models.CharField(max_length=15)),
                ('vote_icon_code', models.CharField(choices=[('Sport', (('1', 'flaticon active person'), ('2', 'flaticon badminton'), ('3', 'flaticon ride bike'), ('4', 'flaticon climbing'), ('5', 'flaticon go fishing'), ('6', 'flaticon golf'), ('7', 'flaticon horse riding'), ('8', 'flaticon flying a kite'), ('9', 'flaticon canoe'), ('10', 'flaticon swimming'), ('11', 'flaticon camping'), ('12', 'flaticon running'), ('13', 'flaticon skateboard'), ('14', 'flaticon ski-lift'), ('15', 'flaticon surfer'), ('16', 'flaticon walking'))), ('Status', (('100', 'fa rocket'), ('101', 'fa mortar-board'), ('102', 'fa flash'), ('103', 'fa heart'), ('104', 'fa hearo')))], max_length=10, null=True)),
                ('vote_icon_name', models.CharField(max_length=100)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Activity')),
            ],
        ),
    ]
