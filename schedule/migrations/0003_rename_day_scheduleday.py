# Generated by Django 4.1.5 on 2023-01-12 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_rename_category_day'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Day',
            new_name='ScheduleDay',
        ),
    ]
