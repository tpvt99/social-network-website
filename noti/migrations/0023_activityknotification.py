# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0020_activitypostcomment'),
        ('noti', '0022_activityjnotification_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityKNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activitypostcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityPostComment')),
                ('noti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti.Notification')),
            ],
        ),
    ]