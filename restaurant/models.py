from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(6)])
    bookingDate = models.DateTimeField()
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title, str(self.price)


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'