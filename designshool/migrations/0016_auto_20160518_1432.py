# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designshool', '0015_auto_20160518_1428'),
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
            field=models.CharField(blank=True, choices=[('Пон', 'Пон'), ('Вт', 'Вт'), ('Ср', 'Ср'), ('Чт', 'Чт'), ('Пт', 'Пт'), ('Сб', 'Сб'), ('Вс', 'Вс'), ('Пон', 'Пон'), ('Вт', 'Вт'), ('Ср', 'Ср'), ('Чт', 'Чт'), ('Пт', 'Пт'), ('Сб', 'Сб'), ('Вс', 'Вс'), ('Пон', 'Пон'), ('Вт', 'Вт'), ('Ср', 'Ср'), ('Чт', 'Чт'), ('Пт', 'Пт'), ('Сб', 'Сб'), ('Вс', 'Вс')], max_length=5, null=True, verbose_name='дни недели'),
        ),
    ]
