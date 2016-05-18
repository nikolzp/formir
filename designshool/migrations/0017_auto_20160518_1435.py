# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designshool', '0016_auto_20160518_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designshool',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach'),
        ),
        migrations.AlterField(
            model_name='designshool',
            name='day_lesson',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='дни недели'),
        ),
        migrations.AlterField(
            model_name='designshool',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='designshool',
            name='price_month',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
