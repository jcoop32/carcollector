from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField('Year')
    color = models.CharField(max_length=200)
    milage = models.IntegerField('Mileage')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.make
    def get_absolute_url(self):
        return reverse('details', kwargs={'car_id': self.id})
