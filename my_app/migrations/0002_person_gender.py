# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default='male', max_length=6),
        ),
    ]
