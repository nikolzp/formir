# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcshool', '0003_auto_20160530_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcshooldet',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach', verbose_name='препод'),
        ),
    ]
