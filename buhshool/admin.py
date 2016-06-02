from django.contrib import admin
from buhshool.models import BuhShoolDet, BuhShoolMain
from django_summernote.admin import SummernoteModelAdmin

class DetInline(admin.TabularInline):
	model = BuhShoolMain.titles.through


class BuhShoolDetAdmin(SummernoteModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')
	radio_fields = {'time_lesson':admin.HORIZONTAL}

class BuhShoolMainAdmin(SummernoteModelAdmin):
	list_display = ('name_course',)
	exclude = ('titles',)
	inlines = [DetInline,]


admin.site.register(BuhShoolDet, BuhShoolDetAdmin)
admin.site.register(BuhShoolMain, BuhShoolMainAdmin)