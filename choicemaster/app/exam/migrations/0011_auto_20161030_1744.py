# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20161030_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exammodel',
            old_name='iterator',
            new_name='result',
        ),
    ]
