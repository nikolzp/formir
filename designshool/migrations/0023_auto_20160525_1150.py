# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designshool', '0022_auto_20160525_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designshooldet',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach', verbose_name='препод'),
        ),
        migrations.RemoveField(
            model_name='designshoolmain',
            name='titles',
        ),
        migrations.AddField(
            model_name='designshoolmain',
            name='titles',
            field=models.ManyToManyField(blank=True, to='designshool.DesignShoolDet', verbose_name='название и описание'),
        ),
    ]