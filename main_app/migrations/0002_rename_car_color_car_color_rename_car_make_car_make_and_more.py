# Generated by Django 4.2.3 on 2023-07-06 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='car_make',
            new_name='make',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='car_model',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='car_year',
            new_name='year',
        ),
    ]
