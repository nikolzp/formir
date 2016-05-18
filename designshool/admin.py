from django.contrib import admin
from designshool.models import DesignShool

class DesignShoolAdmin(admin.ModelAdmin):
	list_display = ('name_course', 'begin_course', 'day_lesson', 'time_lesson', 'coach')


admin.site.register(DesignShool, DesignShoolAdmin)
