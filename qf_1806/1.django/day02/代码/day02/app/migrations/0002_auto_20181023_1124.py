# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
