# Generated by Django 5.0.3 on 2024-03-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_cars_drivetrain'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='car_brand',
            field=models.CharField(default='Ford', max_length=200),
            preserve_default=False,
        ),
    ]
