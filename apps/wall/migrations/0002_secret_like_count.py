# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-24 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
