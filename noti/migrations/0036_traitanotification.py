# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 01:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trait', '0002_auto_20170317_1815'),
        ('noti', '0035_remove_contestanotification_contest'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraitANotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noti', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
                ('trait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trait.Trait')),
            ],
        ),
    ]
