from django.contrib import admin
from designshool.models import DesignShoolDet, DesignShoolMain


class DesignShoolDetAdmin(admin.ModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')

class DesignShoolMainAdmin(admin.ModelAdmin):
	list_display = ('name_course',)
	filter_vertical = ('titles',)


admin.site.register(DesignShoolDet, DesignShoolDetAdmin)
admin.site.register(DesignShoolMain, DesignShoolMainAdmin)