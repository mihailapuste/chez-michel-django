from rest_framework import serializers
from .models import ScheduleDay

class ScheduleDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDay
        fields = [
            'id',
            'day',
            'hours',
            'created_at',
            'updated_at'
            ]

class CreateScheduleDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDay
        fields = ['day', 'hours']

class UpdateScheduleDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDay
        fields = ['hours', 'updated_at']

    hours = serializers.CharField(allow_blank=False, default=None)