# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20171003_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('start_time', models.CharField(max_length=13)),
                ('repeat_mode', models.CharField(max_length=16)),
                ('event_name', models.CharField(default='', max_length=32, primary_key=True, serialize=False)),
                ('event_note', models.CharField(default='', max_length=200)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]
