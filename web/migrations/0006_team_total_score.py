# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_team_total_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='total_score',
            field=models.FloatField(default=0.0),
        ),
    ]
