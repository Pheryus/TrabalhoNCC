# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-08 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0024_auto_20161208_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='trabalho',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]