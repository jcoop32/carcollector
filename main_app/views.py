from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Car
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cars_list(request):
    return render(request, 'cars/cars_list.html', {
        'cars': Car.objects.filter(user=request.user).order_by('id')
    })
@login_required
def car_details(request, car_id):
    return render(request, 'cars/car_details.html', {
        'car': Car.objects.get(id=car_id)
    })
class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'color', 'mileage']

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['make', 'model', 'year', 'color', 'mileage']

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars'

def signup(request):
    error_message = ''
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            # saves user to db
            user = form.save()
            # automatically logins after successful signup
            login(request, user)
            # brings user to car collection
            return redirect('cars')
        else:
            error_message = 'Invalid Sign up. Please try again.'
    # bad POST or GET request, renders signup template
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message,
    })