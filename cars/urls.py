from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.cars, name='cars'),
    path('search/', views.search, name='search'),
    path('<int:id>/', views.car_detail, name='car-detail'),
    path('<str:state>/', views.city_cars, name='state-cars'),
]
