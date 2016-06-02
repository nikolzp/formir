from django.contrib import admin
from langshool.models import LangShoolDet, LangShoolMain
from django_summernote.admin import SummernoteModelAdmin

class DetInline(admin.TabularInline):
	model = LangShoolMain.titles.through


class LangShoolDetAdmin(SummernoteModelAdmin):
	list_display = ('duration_cours', 'piple', 'regime', 'hours_month')


class LangShoolMainAdmin(SummernoteModelAdmin):
	list_display = ('name_course',)
	exclude = ('titles',)
	inlines = [DetInline,]


admin.site.register(LangShoolDet, LangShoolDetAdmin)
admin.site.register(LangShoolMain, LangShoolMainAdmin)