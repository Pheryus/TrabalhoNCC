# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-07 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0018_auto_20161128_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalho',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
