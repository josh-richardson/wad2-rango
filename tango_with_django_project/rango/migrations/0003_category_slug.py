# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170112_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=' '),
            preserve_default=False,
        ),
    ]
