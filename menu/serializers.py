from rest_framework import serializers
from .models import Menu, MenuItem, DietOptions, MenuSections

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'id',
            'name',
            'description',
            'price',
            'section',
            'diet',
            'portion',
            'created_at',
            'updated_at'
            ]

class CreateMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'name',
            'description',
            'price',
            'section',
            'diet',
            'portion'
            ]

class UpdateMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'name',
            'description',
            'price',
            'section',
            'diet',
            'portion'
            'updated_at'
            ]

    name = serializers.CharField(allow_blank=False, default=None)
    description = serializers.CharField(allow_blank=False, default=None)
    price = serializers.DecimalField(max_digits = 6, decimal_places = 2)
    section = serializers.ChoiceField(choices = MenuSections)
    diet = serializers.ChoiceField(choices = DietOptions)
    portion = serializers.IntegerField(min_value = 100, max_value = 1000)


class MenuSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = [
            'id',
            'name',
            'description',
            'items',
            'created_at',
            'updated_at'
            ]

    def get_items(self, obj):
        items = obj.items.all()
        serializer = MenuItemSerializer(items, many=True)
        return serializer.data

class CreateMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'items']

class UpdateMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'items', 'updated_at']

    name = serializers.CharField(allow_blank=False, default=None)
    description = serializers.CharField(allow_blank=False, default=None)
    items = MenuItemSerializer(many=True)