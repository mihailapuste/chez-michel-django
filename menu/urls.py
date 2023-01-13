from django.urls import path

from . import views

urlpatterns = [
    path('menu-items/', views.entrypointMenuItem, name='api.menu_items'),
    path('menu-items/<int:menuItemId>', views.updateMenuItem, name='api.menu_items.update_menu_item'),

    path('menu/', views.entrypointMenu, name='api.menu'),
    path('menu/<int:menuId>', views.updateMenu, name='api.menu.update_menu'),
]