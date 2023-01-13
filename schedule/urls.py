from django.urls import path

from . import views

urlpatterns = [
    path('schedule/', views.entrypointSchedule, name='api.schedule'),
    path('schedule/<int:scheduleDayId>', views.updateScheduleDay, name='api.schedule.update_schedule_day'),
]