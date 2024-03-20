from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Customize admin panel


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html("<img src='{}' width='40' style='border-radius: 50px;' />".format(object.photo.url))

    thumbnail.short_description = 'Image'

    list_display = ('id', 'thumbnail', 'first_name',
                    'last_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name', 'last_name', 'designation')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Teams, TeamAdmin)
