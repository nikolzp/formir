from django.contrib import admin
from designshool.models import DesignShoolDet, DesignShoolMain
from django_summernote.admin import SummernoteModelAdmin


class DetInline(admin.TabularInline):
	model = DesignShoolMain.titles.through

class DesignShoolDetAdmin(SummernoteModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')
	radio_fields = {'time_lesson':admin.HORIZONTAL}


class DesignShoolMainAdmin(SummernoteModelAdmin):
	list_display = ('name_course',)
	exclude = ('titles',)
	inlines = [DetInline,]



admin.site.register(DesignShoolDet, DesignShoolDetAdmin)
admin.site.register(DesignShoolMain, DesignShoolMainAdmin)