from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from cars.models import Cars
from django.core.mail import send_mail
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = f'You have a new message from carsite regarding {subject}'
        message_body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        sender_email = 'rahulns662@gmail.com' 

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            message_body,
            sender_email,
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('pages:contact')


    return render(request, 'pages/contact.html')
