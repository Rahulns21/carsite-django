# Generated by Django 5.0.3 on 2024-03-29 06:46

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_cars_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='car_title', unique=True),
        ),
    ]