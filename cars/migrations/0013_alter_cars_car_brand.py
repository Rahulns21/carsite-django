# Generated by Django 5.0.3 on 2024-03-23 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_alter_cars_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='car_brand',
            field=models.CharField(max_length=200),
        ),
    ]
