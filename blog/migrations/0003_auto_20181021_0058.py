# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-20 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='realated',
            field=models.TextField(blank=True, null=True),
        ),
    ]
