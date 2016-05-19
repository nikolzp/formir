# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('designshool', '0010_auto_20160518_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceDesignShool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, max_length=20, null=True)),
                ('price_month', models.IntegerField(blank=True, max_length=20, null=True)),
                ('sale', models.CharField(blank=True, max_length=20, null=True)),
                ('begin_course', models.CharField(blank=True, max_length=255, null=True, verbose_name='начало занятий')),
                ('day_lesson', models.CharField(blank=True, choices=[('mon', 'Пон'), ('tues', 'Вт'), ('wed', 'Ср'), ('thurs', 'Чт'), ('fri', 'Пт'), ('sat', 'Сб'), ('sun', 'Вс')], max_length=255, null=True, verbose_name='дни недели')),
                ('time_lesson', models.CharField(blank=True, choices=[('9:30', '9:30'), ('10:00', '10:00'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('18:00', '18:00'), ('18:30', '18:30')], max_length=255, null=True, verbose_name='время начала занятий')),
                ('place_course', models.CharField(blank=True, max_length=255, null=True)),
                ('coach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach')),
            ],
        ),
        migrations.RemoveField(
            model_name='designshool',
            name='begin_course',
        ),
        migrations.RemoveField(
            model_name='designshool',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='designshool',
            name='day_lesson',
        ),
        migrations.RemoveField(
            model_name='designshool',
            name='place_course',
        ),
        migrations.RemoveField(
            model_name='designshool',
            name='price',
        ),
        migrations.RemoveField(
            model_name='designshool',
            name='price_month',
        ),
        migrations.RemoveField(
            model_name='designshool',
            name='sale',
        ),
        migrations.RemoveField(
            model_name='designshool',
            name='time_lesson',
        ),
    ]