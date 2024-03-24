from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

class Cars(models.Model):
    class Meta:
        verbose_name_plural = 'Cars'
        ordering = ['created_date']

    def __str__(self) -> str:
        return f'{self.car_title} - {self.car_reg_number}'
    
    indian_states = (
    ('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'),
    ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('CT', 'Chhattisgarh'), ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'),
    ('KL', 'Kerala'), ('LD', 'Ladakh'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'),
    ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'),
    ('OD', 'Odisha'), ('PY', 'Puducherry'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'),
    ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal'),
    )

    features_choices = (
        ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Alarm System', 'Alarm System'),
        ('Anti-lock Braking System (ABS)', 'Anti-lock Braking System (ABS)'), ('Audio Interface', 'Audio Interface'), ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Bluetooth Handset', 'Bluetooth Handset'), ('Central Locking System', 'Central Locking System'), ('Cruise Control', 'Cruise Control'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'), ('Seat Heating', 'Seat Heating'), ('Wind Deflector', 'Wind Deflector'),
    )

    door_choices = (
        (1, '1'), (2, '2'), (3, '3'),
        (4, '4'), (5, '5'), (7, '7'),
        (8, '8'), (9, '9'), (10, '10'),
    )

    transmission_choices = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    )

    fuel_choices = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'), 
        ('CNG', 'CNG'),
        ('Electric', 'Electric'),
    )

    drivetrain_choices = (
        ('Front Wheel Drive (FWD)', 'Front Wheel Drive (FWD)'),
        ('Rear Wheel Drive (RWD)', 'Rear Wheel Drive (RWD)'),
        ('All Wheel Drive (AWD)', 'All Wheel Drive (AWD)'),
        ('4 Wheel Drive (4WD)', '4 Wheel Drive (4WD)'),
    )

    condition_choices = (
        ('New', 'New'),
        ('Used', 'Used'),
    )

    year_choice = []
    for y in range(datetime.now().year, 1949, -1):
        year_choice.append((y, y))
    
    car_brand = models.CharField(max_length=200)
    car_title = models.CharField(max_length=200)
    state = models.CharField(choices=indian_states, max_length=200)
    city = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.PositiveIntegerField(('year'), choices=year_choice)
    condition = models.CharField(choices=condition_choices, max_length=200)
    price = models.PositiveIntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=2000)
    body_style = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    drivetrain = models.CharField(choices=drivetrain_choices, max_length=500)
    transmission_type = models.CharField(choices=transmission_choices, max_length=200)
    interior = models.CharField(max_length=200)
    kilometers = models.PositiveIntegerField()
    doors = models.PositiveIntegerField(choices=door_choices)
    passengers = models.PositiveIntegerField()
    car_reg_number = models.CharField(max_length=200)
    mileage = models.PositiveIntegerField()
    fuel_type = models.CharField(choices=fuel_choices, max_length=200)
    no_of_owners = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
