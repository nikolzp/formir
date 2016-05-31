 # -*- coding: utf-8 -*-
from django.db import models
from coaches.models import Coach

class LangShoolDet(models.Model):
	duration_cours = models.CharField(verbose_name='продолжительность курса', max_length=100, null=True, blank=True)
	price = models.IntegerField(verbose_name='цена за курс', null=True, blank=True)
	price_month = models.IntegerField(verbose_name='цена за месяц', null=True, blank=True)
	sale = models.CharField(verbose_name='скидка', max_length=20, null=True, blank=True)
	piple = models.CharField(verbose_name='количество человек', max_length=20, null=True, blank=True)
	regime = models.CharField(verbose_name='режим занятий', max_length=30, null=True, blank=True)
	hours_month = models.CharField(verbose_name='часов в месяц', max_length=20, null=True, blank=True)
		
	def __str__(self):
		s = '%s грн || %s || %s ' % (self.price_month, self.piple, self.hours_month)
		return s


class LangShoolMain(models.Model):
	name_course = models.CharField(verbose_name='название курса', max_length=255)
	description = models.TextField(verbose_name='развернутое описание', null=True, blank=True)
	titles = models.ManyToManyField(LangShoolDet, verbose_name='название и описание', blank=True)
	def __str__ (self):
		return self.name_course