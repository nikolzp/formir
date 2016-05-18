# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designshool', '0013_auto_20160518_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayLessonDesignShool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_lesson', models.CharField(blank=True, choices=[('mon', 'Пон'), ('tues', 'Вт'), ('wed', 'Ср'), ('thurs', 'Чт'), ('fri', 'Пт'), ('sat', 'Сб'), ('sun', 'Вс')], max_length=5, null=True, verbose_name='дни недели')),
            ],
        ),
        migrations.RemoveField(
            model_name='choicedesignshool',
            name='day_lesson',
        ),
        migrations.AlterField(
            model_name='choicedesignshool',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach'),
        ),
        migrations.AddField(
            model_name='choicedesignshool',
            name='day_lesson_start',
            field=models.ManyToManyField(blank=True, null=True, to='designshool.DayLessonDesignShool'),
        ),
    ]
