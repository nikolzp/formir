from django.contrib import admin
from graphshool.models import GraphShoolDet, GraphShoolMain


class GraphShoolDetAdmin(admin.ModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')

class GraphShoolMainAdmin(admin.ModelAdmin):
	list_display = ('name_course',)
	filter_vertical = ('titles',)


admin.site.register(GraphShoolDet, GraphShoolDetAdmin)
admin.site.register(GraphShoolMain, GraphShoolMainAdmin)