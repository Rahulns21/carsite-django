from django.shortcuts import render
from .models import *
from cars.models import Cars

def home(request):
    teams = Teams.objects.all()
    featured_cars = Cars.objects.order_by('-is_featured').filter(is_featured=True)
    all_cars = Cars.objects.order_by('-is_featured').all()
    search_brand = Cars.objects.order_by('car_brand').values_list('car_brand', flat=True).distinct()
    search_car = Cars.objects.order_by('car_title').values_list('car_title', flat=True).distinct()
    search_location = Cars.objects.order_by('city').values_list('city', flat=True).distinct()
    search_year = Cars.objects.order_by('-year').values_list('year', flat=True).distinct()
    search_body = Cars.objects.order_by('body_style').values_list('body_style', flat=True).distinct()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'search_brand': search_brand,
        'search_car': search_car,
        'search_location': search_location,
        'search_year': search_year,
        'search_body': search_body,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
