# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0004_auto_20161025_0340'),
        ('Portal', '0025_auto_20161208_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabalho',
            name='id',
        ),
        migrations.AddField(
            model_name='trabalho',
            name='turma',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Usuarios.Turma'),
            preserve_default=False,
        ),
    ]