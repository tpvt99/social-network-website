# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 10:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('act', '0003_act_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('been_vote', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='act',
            name='activity',
        ),
        migrations.AddField(
            model_name='act',
            name='vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='actvote',
            name='act',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='act_actvote_act', to='act.Act'),
        ),
        migrations.AddField(
            model_name='actvote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='actvote',
            unique_together=set([('act', 'user')]),
        ),
    ]
