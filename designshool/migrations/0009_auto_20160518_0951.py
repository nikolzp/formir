# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designshool', '0008_auto_20160518_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designshool',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach'),
        ),
    ]