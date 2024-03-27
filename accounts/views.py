from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as user_login, authenticate, logout as user_logout
from django.contrib.auth.models import User
from .decorators import user_not_authenticated
from django.views.decorators.csrf import csrf_protect
from contacts.models import Contact
from cars.models import Cars

@user_not_authenticated
def login(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']

        try:
            username = User.objects.get(email=username_or_email).username
        except User.DoesNotExist:
            username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            user_login(request, user)
            return redirect('pages:home')
        else: 
            messages.error(request, 'Invalid login credentials or User doesn\'t exist!')
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')

@user_not_authenticated
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST.get('password', '')
        confirm_password = request.POST['confirm_password']

        if len(password) < 8:
            messages.error(request, 'Password must have minimum 8 characters')
            return redirect('accounts:register')
        
        if not password == confirm_password:
            messages.error(request, 'Passwords doesn\'t match')
            return redirect('accounts:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists! Choose a different one')
            return redirect('accounts:register')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                login(request, user)
                return redirect('pages:home')
    else:
        return render(request, 'accounts/register.html')

@login_required
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-created_date').filter(user=request.user)
    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)

@csrf_protect
def logout(request):
    if request.method == 'POST':
        user_logout(request)
    return redirect('pages:home')