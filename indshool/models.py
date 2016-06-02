 # -*- coding: utf-8 -*-
from django.db import models


class IndShoolMain(models.Model):
	name_course = models.CharField(verbose_name='название курса', max_length=255)
	deskr = models.CharField(verbose_name='описание', max_length=255, null=True, blank=True)
	price = models.CharField(verbose_name='цена за курс', max_length=50, null=True, blank=True)
	hours = models.CharField(verbose_name='кол-во ак.час', max_length=50, blank=True)
	def __str__ (self):
		return self.name_course
	class Meta:
		verbose_name_plural = "Индивидуальные Занятия"