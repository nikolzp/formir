from django.contrib import admin
from pcshool.models import PCShoolDet, PCShoolMain


class PCShoolDetAdmin(admin.ModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')

class PCShoolMainAdmin(admin.ModelAdmin):
	list_display = ('name_course',)
	filter_vertical = ('titles',)


admin.site.register(PCShoolDet, PCShoolDetAdmin)
admin.site.register(PCShoolMain, PCShoolMainAdmin)