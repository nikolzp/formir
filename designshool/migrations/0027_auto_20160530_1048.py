# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designshool', '0026_auto_20160526_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designshooldet',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach', verbose_name='препод'),
        ),
    ]
