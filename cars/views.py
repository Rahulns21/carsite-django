from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import Cars


def cars(request):
    cars = Cars.objects.order_by('-is_featured')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    search_car = Cars.objects.order_by('car_title').values_list('car_title', flat=True).distinct()
    search_brand = Cars.objects.order_by('car_brand').values_list('car_brand', flat=True).distinct()
    search_location = Cars.objects.order_by('city').values_list('city', flat=True).distinct()
    search_year = Cars.objects.order_by('-year').values_list('year', flat=True).distinct()
    search_body = Cars.objects.order_by('body_style').values_list('body_style', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'search_car': search_car,
        'search_brand': search_brand,
        'search_location': search_location,
        'search_year': search_year,
        'search_body': search_body,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    car_detail = get_object_or_404(Cars, pk=id)
    data = {'car_detail': car_detail}
    return render(request, 'cars/car_detail.html', data)

def city_cars(request, city):
    city_cars = Cars.objects.order_by('-is_featured').filter(city=city)
    data = {'city_cars': city_cars}
    return render(request, 'cars/city_cars.html', data)

def search(request):
    cars = Cars.objects.order_by('-is_featured')

    search_brand = Cars.objects.order_by('car_brand').values_list('car_brand', flat=True).distinct()
    search_car = Cars.objects.order_by('car_title').values_list('car_title', flat=True).distinct()
    search_location = Cars.objects.order_by('city').values_list('city', flat=True).distinct()
    search_year = Cars.objects.order_by('-year').values_list('year', flat=True).distinct()
    search_body = Cars.objects.order_by('body_style').values_list('body_style', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(car_title__icontains=keyword)

    if 'car_title' in request.GET:
        car_title = request.GET['car_title']
        if car_title:
            cars = cars.filter(car_title__iexact=car_title)

    if 'car_brand' in request.GET:
        car_brand = request.GET['car_brand']
        if car_brand:
            cars = cars.filter(car_brand__iexact=car_brand)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if city:
            body_style = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'search_brand': search_brand,
        'search_car': search_car,
        'search_location': search_location,
        'search_year': search_year,
        'search_body': search_body,
    }
    return render(request, 'cars/search.html', data)