# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_auto_20161030_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodel',
            name='subject',
            field=models.CharField(default='Type Subject', max_length=100),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='topic',
            field=models.CharField(default='Type Topic', max_length=100),
        ),
    ]
