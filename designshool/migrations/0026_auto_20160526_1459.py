# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designshool', '0025_auto_20160526_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designshooldet',
            name='short_description',
        ),
        migrations.AddField(
            model_name='designshooldet',
            name='duration_cours',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='продолжительность курса'),
        ),
        migrations.AlterField(
            model_name='designshooldet',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach', verbose_name='препод'),
        ),
    ]
