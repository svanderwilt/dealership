# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
# - __str__ method to print a car make object
    def __str__(self) -> str:
        return self.name


class CarModel(models.Model):
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
# - Name
    name = models.CharField(max_length=100)
# - Type (CharField with a choices argument to provide limited choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe')
    ]
# such as Sedan, SUV, WAGON, etc.)
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
  
    def __str__(self):
        return self.name  # Return the name as the string representation
