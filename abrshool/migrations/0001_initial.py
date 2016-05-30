# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbrShoolDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_cours', models.CharField(blank=True, max_length=100, null=True, verbose_name='продолжительность курса')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='цена за курс')),
                ('price_month', models.IntegerField(blank=True, null=True, verbose_name='цена за месяц')),
                ('sale', models.CharField(blank=True, max_length=20, null=True, verbose_name='скидка')),
                ('begin_course', models.CharField(blank=True, max_length=255, null=True, verbose_name='начало занятий')),
                ('day_lesson', models.CharField(blank=True, max_length=20, null=True, verbose_name='дни недели')),
                ('time_lesson', models.CharField(blank=True, choices=[('9:30', '9:30'), ('10:00', '10:00'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('18:00', '18:00'), ('18:30', '18:30')], max_length=5, null=True, verbose_name='время начала занятий')),
                ('place_course', models.CharField(blank=True, max_length=255, null=True, verbose_name='филиал')),
                ('coach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.Coach', verbose_name='препод')),
            ],
        ),
        migrations.CreateModel(
            name='AbrShoolMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course', models.CharField(max_length=255, verbose_name='название курса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='развернутое описание')),
                ('titles', models.ManyToManyField(blank=True, to='abrshool.AbrShoolDet', verbose_name='название и описание')),
            ],
        ),
    ]
