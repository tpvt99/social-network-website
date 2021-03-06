# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-25 13:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitySport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_sport', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='time',
        ),
        migrations.AddField(
            model_name='activity',
            name='time_begin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='time_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_activity_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activitysport',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_activitysport_activity', to='activity.Activity'),
        ),
    ]
