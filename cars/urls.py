from django.urls import path, re_path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.cars, name='cars'),
    path('search/', views.search, name='search'),
    path('<str:slug>/', views.car_detail, name='car-detail'),
]
