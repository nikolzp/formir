# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('designshool', '0014_auto_20160518_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choicedesignshool',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='choicedesignshool',
            name='day_lesson_start',
        ),
        migrations.RemoveField(
            model_name='designshool',
            name='choice_detail',
        ),
        migrations.AddField(
            model_name='designshool',
            name='begin_course',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='начало занятий'),
        ),
        migrations.AddField(
            model_name='designshool',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach'),
        ),
        migrations.AddField(
            model_name='designshool',
            name='day_lesson',
            field=models.CharField(blank=True, choices=[('Пон', 'Пон'), ('Вт', 'Вт'), ('Ср', 'Ср'), ('Чт', 'Чт'), ('Пт', 'Пт'), ('Сб', 'Сб'), ('Вс', 'Вс')], max_length=5, null=True, verbose_name='дни недели'),
        ),
        migrations.AddField(
            model_name='designshool',
            name='place_course',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='designshool',
            name='price',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='designshool',
            name='price_month',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='designshool',
            name='sale',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='designshool',
            name='time_lesson',
            field=models.CharField(blank=True, choices=[('9:30', '9:30'), ('10:00', '10:00'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('18:00', '18:00'), ('18:30', '18:30')], max_length=5, null=True, verbose_name='время начала занятий'),
        ),
        migrations.DeleteModel(
            name='ChoiceDesignShool',
        ),
        migrations.DeleteModel(
            name='DayLessonDesignShool',
        ),
    ]
