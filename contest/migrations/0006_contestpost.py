# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 15:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0005_contest_contest_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contest_contestpost_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
