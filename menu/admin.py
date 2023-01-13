from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'section', 'price', 'diet', 'created_at', 'updated_at']

admin.site.register(MenuItem, MenuItemAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']

admin.site.register(Menu, MenuAdmin)