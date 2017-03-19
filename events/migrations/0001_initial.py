# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 02:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0012_eventpost_eventpostcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('privacy', models.CharField(max_length=100, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_eventspost_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventsPostFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('eventspost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_eventspostfriend_eventspost', to='events.EventsPost')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_eventspostfriend_friend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]