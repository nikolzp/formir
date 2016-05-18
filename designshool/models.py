 # -*- coding: utf-8 -*-
from django.db import models
from coaches.models import Coach


class DesignShool(models.Model):
	name_course = models.CharField(verbose_name='название курса', max_length=255)
	description = models.TextField(verbose_name='развернутое описание', null=True, blank=True)
	short_description = models.TextField(verbose_name='заметки', null=True, blank=True)
	price = models.IntegerField(verbose_name='цена за курс', null=True, blank=True)
	price_month = models.IntegerField(verbose_name='цена за месяц', null=True, blank=True)
	sale = models.CharField(verbose_name='скидка', max_length=20, null=True, blank=True)
	begin_course = models.CharField(verbose_name='начало занятий', max_length=255, null=True, blank=True)
	day_lesson = models.CharField(verbose_name='дни недели', max_length=20, null=True, blank=True)
	time_lesson = models.CharField(verbose_name='время начала занятий', max_length=5, null=True, blank=True, 
		choices=(('9:30','9:30'),('10:00','10:00'),('12:00','12:00'),('12:30','12:30'),('13:00','13:00'),
			('15:00','15:00'),('15:30','15:30'),('16:00','16:00'),('18:00','18:00'),('18:30','18:30')))
	place_course = models.CharField(verbose_name='филиал', max_length=255, null=True, blank=True)
	coach = models.ForeignKey(Coach, verbose_name='препод', null=True, blank=True)
		
	def __str__(self):
		return self.name_course