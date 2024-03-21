from django.contrib import admin
from django.utils.html import format_html
from .models import *


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html("<img src='{}' width='50' style='border-radius: 5px;' />".format(object.car_photo.url))

    thumbnail.short_description = 'Image'

    list_display = ('id', 'car_title', 'thumbnail', 'state', 'car_reg_number', 'is_featured', 'price')
    list_display_links = ('car_title',)
    list_editable = ('is_featured', 'price')
    search_fields = ('car_title', 'state', 'city', 'model', 'car_reg_number', 'body_style')
    list_filter = ('state', 'body_style', 'fuel_type')


admin.site.register(Cars, TeamAdmin)
