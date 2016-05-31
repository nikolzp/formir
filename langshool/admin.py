from django.contrib import admin
from langshool.models import LangShoolDet, LangShoolMain


class LangShoolDetAdmin(admin.ModelAdmin):
	list_display = ('duration_cours', 'piple', 'regime', 'hours_month')

class LangShoolMainAdmin(admin.ModelAdmin):
	list_display = ('name_course',)
	filter_vertical = ('titles',)


admin.site.register(LangShoolDet, LangShoolDetAdmin)
admin.site.register(LangShoolMain, LangShoolMainAdmin)