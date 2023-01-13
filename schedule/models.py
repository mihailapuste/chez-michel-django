from django.db import models
from main.models import TimestampModel

# Create your models here.
class ScheduleDay(TimestampModel):

    class WeekDays(models.IntegerChoices):
        MONDAY = 0
        TUESDAY = 1
        WEDNESDAY = 2
        THURSDAY = 3
        FRIDAY = 4
        SATURDAY = 5
        SUNDAY = 6

    day = models.IntegerField(choices=WeekDays.choices)
    hours = models.TextField()