# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20170101_0840'),
        ('noti', '0010_auto_20170101_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventENotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('eventparticipants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventParticipants')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='EventFNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('eventparticipants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventParticipants')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
    ]