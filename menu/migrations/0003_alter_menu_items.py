# Generated by Django 4.1.5 on 2023-01-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_menu_section_menu_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='items',
            field=models.ManyToManyField(blank=True, to='menu.menuitem'),
        ),
    ]