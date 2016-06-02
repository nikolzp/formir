from django.db import models

class Coach(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	phone = models.CharField(max_length=20, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.surname

	class Meta:
		verbose_name_plural = "Преподы"