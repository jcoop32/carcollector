from django.shortcuts import render
from .models import Car
# Create your views here.
def home(request):
    return render(request, 'home.html')

def cars_list(request):
    return render(request, 'cars/cars_list.html', {
        'cars': Car.objects.all()
    })
 