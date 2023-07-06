from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField('Year')
    color = models.CharField(max_length=200)
    milage = models.IntegerField('Mileage')
    def __str__(self):
        return self.make
