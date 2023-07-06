# Generated by Django 4.2.3 on 2023-07-06 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_make', models.CharField(max_length=200)),
                ('car_model', models.CharField(max_length=200)),
                ('car_year', models.IntegerField(verbose_name='Year')),
                ('car_color', models.CharField(max_length=200)),
            ],
        ),
    ]
