# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designshool', '0033_auto_20160531_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='designshooldet',
            options={'verbose_name_plural': ''},
        ),
        migrations.AlterModelOptions(
            name='designshoolmain',
            options={'verbose_name_plural': 'Школа Дизайна'},
        ),
        migrations.AlterField(
            model_name='designshooldet',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach', verbose_name='препод'),
        ),
    ]
