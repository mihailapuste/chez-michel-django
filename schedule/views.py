from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view


from .models import ScheduleDay

from .serializers import (
    ScheduleDaySerializer,
    CreateScheduleDaySerializer,
    UpdateScheduleDaySerializer
)

@api_view(['GET', 'POST'])
def entrypointSchedule(request: Request) -> Response:
    if request.method == 'GET':
        return getScheduleDays(request)

    if (request.method == 'POST'):
        return addScheduleDay(request)

    return APIException('Method not supported', status.HTTP_400_BAD_REQUEST)


def getScheduleDays(request: Request) -> Response:
    items = ScheduleDay.objects.filter(
        deleted_at=None,
    ).all()

    serializer = ScheduleDaySerializer(items, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

def addScheduleDay(request: Request) -> Response:
    serializer = CreateScheduleDaySerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    schedule_day = serializer.save()

    return Response(ScheduleDaySerializer(schedule_day).data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def updateScheduleDay(request: Request, scheduleDayId: int) -> Response:
    serializer = UpdateScheduleDaySerializer(
        ScheduleDay.objects.get(id=scheduleDayId),
        request.data,
        partial=True,
        context={ 'request': request }
    )
    serializer.is_valid(raise_exception=True)

    schedule_day = serializer.save()

    return Response(ScheduleDaySerializer(schedule_day).data, status=status.HTTP_200_OK)
