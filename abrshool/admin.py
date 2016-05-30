from django.contrib import admin
from abrshool.models import AbrShoolDet, AbrShoolMain


class AbrShoolDetAdmin(admin.ModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')

class AbrShoolMainAdmin(admin.ModelAdmin):
	list_display = ('name_course',)
	filter_vertical = ('titles',)


admin.site.register(AbrShoolDet, AbrShoolDetAdmin)
admin.site.register(AbrShoolMain, AbrShoolMainAdmin)