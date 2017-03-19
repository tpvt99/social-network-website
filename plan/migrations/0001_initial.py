# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 12:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantMoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_join', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_participantmoreinfo_person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('des', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('time', models.DateTimeField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('place', models.CharField(max_length=100, null=True)),
                ('street', models.CharField(max_length=100, null=True)),
                ('share', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_plan_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlanParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participants', models.ManyToManyField(related_name='plan_planparticipants_participants', through='plan.ParticipantMoreInfo', to=settings.AUTH_USER_MODEL)),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plan.Plan')),
            ],
        ),
        migrations.AddField(
            model_name='participantmoreinfo',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_participantmoreinfo_plan', to='plan.Plan'),
        ),
        migrations.AddField(
            model_name='participantmoreinfo',
            name='planparticipants',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_participantmoreinfo_participants', to='plan.PlanParticipants'),
        ),
    ]
