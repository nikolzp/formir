from django.contrib import admin
from indshool.models import IndShoolMain


class IndShoolMainAdmin(admin.ModelAdmin):
	list_display = ('name_course', 'price', 'hours')


admin.site.register(IndShoolMain, IndShoolMainAdmin)
