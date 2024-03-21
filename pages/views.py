from django.shortcuts import render
from .models import *
from cars.models import Cars

def home(request):
    teams = Teams.objects.all()
    featured_cars = Cars.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Cars.objects.order_by('-created_date').all()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')