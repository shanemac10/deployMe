# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-24 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='alias',
            new_name='last_name',
        ),
    ]
