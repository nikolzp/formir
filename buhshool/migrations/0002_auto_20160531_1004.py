# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buhshool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buhshooldet',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach', verbose_name='препод'),
        ),
    ]
