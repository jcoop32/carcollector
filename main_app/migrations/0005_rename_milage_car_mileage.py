# Generated by Django 4.2.3 on 2023-07-08 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_car_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='milage',
            new_name='mileage',
        ),
    ]
