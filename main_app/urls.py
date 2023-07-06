from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_list, name='cars'),
    path('cars/<int:car_id>', views.car_details, name='details'),
    path('cars/create/', views.CarCreate.as_view(), name='car_create')
]
