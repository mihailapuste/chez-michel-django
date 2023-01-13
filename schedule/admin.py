from django.contrib import admin
from .models import ScheduleDay

class ScheduleDayAdmin(admin.ModelAdmin):
    list_display = ['id', 'day', 'hours', 'created_at', 'updated_at', 'deleted_at']

admin.site.register(ScheduleDay, ScheduleDayAdmin)