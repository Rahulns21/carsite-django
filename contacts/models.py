from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self) -> str:
        return self.email
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=250)
    car_title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = PhoneNumberField()
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
