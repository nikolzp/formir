from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    search_fields = ['surname']
    list_display = ('surname', 'name')


admin.site.register(Coach, CoachAdmin)