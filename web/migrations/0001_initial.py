# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('score', models.FloatField(default=0.0)),
                ('member_1', models.CharField(max_length=100)),
                ('member_2', models.CharField(blank=True, max_length=100)),
                ('member_3', models.CharField(blank=True, max_length=100)),
                ('member_4', models.CharField(blank=True, max_length=100)),
                ('email_1', models.EmailField(max_length=254)),
                ('email_2', models.EmailField(blank=True, max_length=254)),
                ('email_3', models.EmailField(blank=True, max_length=254)),
                ('email_4', models.EmailField(blank=True, max_length=254)),
                ('size_1', models.CharField(blank=True, choices=[('', 'None'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='', max_length=1, null=True)),
                ('size_2', models.CharField(blank=True, choices=[('', 'None'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='', max_length=1, null=True)),
                ('size_3', models.CharField(blank=True, choices=[('', 'None'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='', max_length=1, null=True)),
                ('size_4', models.CharField(blank=True, choices=[('', 'None'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='', max_length=1, null=True)),
                ('diet', models.CharField(blank=True, max_length=1000)),
                ('code', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('last_login', models.DateTimeField(null=True)),
            ],
        ),
    ]