from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from main.models import TimestampModel

class MenuSections(models.TextChoices):
        APPETIZERS = 'A'
        MAINS = 'M'
        DESERTS = 'D'

class DietOptions(models.TextChoices):
        VEGAN = 'V'
        VEGETARIAN = 'VG'
        DAIRY_FREE = 'DF'
        GLUTEN_FREE = 'GF'

class MenuItem(TimestampModel):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    section = models.CharField(max_length=1, choices=MenuSections.choices)
    diet = models.CharField(max_length=2, choices=DietOptions.choices, blank=True)
    portion = models.IntegerField(
        validators=[
            MaxValueValidator(1000),
            MinValueValidator(100)
        ]
    )

    def __str__(self):
        return self.name

class Menu(TimestampModel):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=254)
    items = models.ManyToManyField(MenuItem, blank=True)

    def __str__(self):
        return self.name