from django.contrib import admin
from buhshool.models import BuhShoolDet, BuhShoolMain


class BuhShoolDetAdmin(admin.ModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')

class BuhShoolMainAdmin(admin.ModelAdmin):
	list_display = ('name_course',)
	filter_vertical = ('titles',)


admin.site.register(BuhShoolDet, BuhShoolDetAdmin)
admin.site.register(BuhShoolMain, BuhShoolMainAdmin)