# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20161026_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(default='Sin materia', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(default='Sin tema', max_length=100),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_reported',
            field=models.BooleanField(default=False),
        ),
    ]