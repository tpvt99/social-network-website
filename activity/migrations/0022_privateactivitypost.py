# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 11:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0021_auto_20170103_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateActivityPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_privateactivitypost_activity', to='activity.Activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_privateactivitypost_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
