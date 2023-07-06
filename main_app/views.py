from django.shortcuts import render
from .models import Car
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_list(request):
    return render(request, 'cars/cars_list.html', {
        'cars': Car.objects.all()
    })
 
def car_details(request, car_id):
    return render(request, 'cars/car_details.html', {
        'car': Car.objects.get(id=car_id)
    })
  