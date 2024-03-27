from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'car_title', 'price', 'email', 'phone', 'city', 'state', 'created_date')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('email', 'phone', 'car_title', 'first_name', 'last_name')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)