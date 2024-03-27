from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

@login_required
def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = request.user
        car_id = request.POST['car_id']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        price = request.POST['price']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)

        if has_contacted:
            messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you')
            return redirect('/cars/'+car_id)

        contact = Contact(first_name=first_name, last_name=last_name, user=user, car_id=car_id,
                customer_need=customer_need, car_title=car_title, city=city, state=state, email=email, 
                phone=phone, message=message)
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            'New Car Inquiry',
            'You have a new inquiry for ' + car_title + '. Please login to your admin panel for more info',
            'rahulns662@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'You request has been submitted, we will get in touch with you shortly.')
        return redirect('/cars/'+car_id)

