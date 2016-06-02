from django.contrib import admin
from pcshool.models import PCShoolDet, PCShoolMain
from django_summernote.admin import SummernoteModelAdmin

class DetInline(admin.TabularInline):
	model = PCShoolMain.titles.through


class PCShoolDetAdmin(SummernoteModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')
	radio_fields = {'time_lesson':admin.HORIZONTAL}

class PCShoolMainAdmin(SummernoteModelAdmin):
	list_display = ('name_course',)
	exclude = ('titles',)
	inlines = [DetInline,]


admin.site.register(PCShoolDet, PCShoolDetAdmin)
admin.site.register(PCShoolMain, PCShoolMainAdmin)