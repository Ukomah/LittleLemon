from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    no_of_guest = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(6)])
    bookingDate = models.DateTimeField()
    
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField(max_length=1000, default='') 

    def __str__(self):
        template = '{0.title} {0.price}'
        return template.format(self)

