# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 17:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friend', '0002_auto_20160904_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_time', models.DateTimeField(auto_now_add=True)),
                ('is_friend', models.BooleanField(default=False)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_addfriend_inviter', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_addfriend_receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='addfriendmodel',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='addfriendmodel',
            name='inviter',
        ),
        migrations.RemoveField(
            model_name='addfriendmodel',
            name='receiver',
        ),
        migrations.DeleteModel(
            name='AddFriendModel',
        ),
        migrations.AlterUniqueTogether(
            name='addfriend',
            unique_together=set([('inviter', 'receiver')]),
        ),
    ]
