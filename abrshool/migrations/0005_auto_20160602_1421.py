# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abrshool', '0004_auto_20160531_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abrshooldet',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach', verbose_name='препод'),
        ),
    ]