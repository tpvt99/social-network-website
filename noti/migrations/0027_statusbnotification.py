# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_statuscomment'),
        ('noti', '0026_statusanotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusBNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noti', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.Status')),
                ('statuscomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.StatusComment')),
            ],
        ),
    ]
