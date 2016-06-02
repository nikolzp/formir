from django.contrib import admin
from graphshool.models import GraphShoolDet, GraphShoolMain
from django_summernote.admin import SummernoteModelAdmin

class DetInline(admin.TabularInline):
	model = GraphShoolMain.titles.through


class GraphShoolDetAdmin(SummernoteModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')
	radio_fields = {'time_lesson':admin.HORIZONTAL}

class GraphShoolMainAdmin(SummernoteModelAdmin):
	list_display = ('name_course',)
	exclude = ('titles',)
	inlines = [DetInline,]


admin.site.register(GraphShoolDet, GraphShoolDetAdmin)
admin.site.register(GraphShoolMain, GraphShoolMainAdmin)