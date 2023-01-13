from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view

from .models import Menu, MenuItem

from .serializers import (
    MenuItemSerializer,
    CreateMenuItemSerializer,
    UpdateMenuItemSerializer,
    MenuSerializer,
    CreateMenuSerializer,
    UpdateMenuSerializer
)

# Menu Item Views

@api_view(['GET', 'POST'])
def entrypointMenuItem(request: Request) -> Response:
    if request.method == 'GET':
        return getMenuItems(request)

    if (request.method == 'POST'):
        return addMenuItem(request)

    return APIException('Method not supported', status.HTTP_400_BAD_REQUEST)

def getMenuItems(request: Request) -> Response:
    menuItems = MenuItem.objects.filter(
        deleted_at=None,
    ).all()

    serializer = MenuItemSerializer(menuItems, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

def addMenuItem(request: Request) -> Response:
    serializer = CreateMenuItemSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    menuItem = serializer.save()

    return Response(MenuItemSerializer(menuItem).data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def updateMenuItem(request: Request, menuItemId: int) -> Response:
    serializer = UpdateMenuItemSerializer(
        MenuItem.objects.get(id=menuItemId),
        request.data,
        partial=True,
        context={ 'request': request }
    )
    serializer.is_valid(raise_exception=True)

    menuItem = serializer.save()

    return Response(MenuItemSerializer(menuItem).data, status=status.HTTP_200_OK)

# Menu Views

@api_view(['GET', 'POST'])
def entrypointMenu(request: Request) -> Response:
    if request.method == 'GET':
        return getMenus(request)

    if (request.method == 'POST'):
        return addMenu(request)

    return APIException('Method not supported', status.HTTP_400_BAD_REQUEST)


def getMenus(request: Request) -> Response:
    menus = Menu.objects.filter(
        deleted_at=None,
    ).all()

    serializer = MenuSerializer(menus, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

def addMenu(request: Request) -> Response:
    serializer = CreateMenuSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    menu = serializer.save()

    return Response(MenuSerializer(menu).data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def updateMenu(request: Request, menuId: int) -> Response:
    serializer = UpdateMenuSerializer(
        Menu.objects.get(id=menuId),
        request.data,
        partial=True,
        context={ 'request': request }
    )
    serializer.is_valid(raise_exception=True)

    menu = serializer.save()

    return Response(MenuSerializer(menu).data, status=status.HTTP_200_OK)