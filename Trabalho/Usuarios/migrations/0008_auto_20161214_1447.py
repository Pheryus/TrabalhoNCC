# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0007_remove_turma_alunos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='professor',
            field=models.IntegerField(),
        ),
    ]