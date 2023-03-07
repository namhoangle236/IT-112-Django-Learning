from django.shortcuts import render
from .models import Car  # importing the Car class from models.py

# Create your views here.
# Function to Function to get all 'cars' from db, then render template, and passing 'cars' to be used in html
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

# Function to get 'car' from db based on 'car_id' passed in the URL, then render template, also passing 'car' to be used in html
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car_detail.html', {'car': car})
