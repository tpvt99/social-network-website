# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-17 15:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import trait.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait_type', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to=trait.models.upload_trait_picture)),
                ('user_receive', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trait_trait_user_receive', to=settings.AUTH_USER_MODEL)),
                ('user_send', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trait_trait_user_send', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
