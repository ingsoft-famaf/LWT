# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='is_reported',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]