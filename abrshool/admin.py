from django.contrib import admin
from abrshool.models import AbrShoolDet, AbrShoolMain
from django_summernote.admin import SummernoteModelAdmin

class DetInline(admin.TabularInline):
	model = AbrShoolMain.titles.through


class AbrShoolDetAdmin(SummernoteModelAdmin):
	list_display = ('duration_cours', 'begin_course', 'day_lesson', 'time_lesson', 'coach')
	radio_fields = {'time_lesson':admin.HORIZONTAL}

class AbrShoolMainAdmin(SummernoteModelAdmin):
	list_display = ('name_course',)
	exclude = ('titles',)
	inlines = [DetInline,]


admin.site.register(AbrShoolDet, AbrShoolDetAdmin)
admin.site.register(AbrShoolMain, AbrShoolMainAdmin)