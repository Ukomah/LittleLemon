from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(6)])
    BookingDate = models.DateTimeField()
    
    def __str__(self):
        return self.Name

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Inventory = models.IntegerField()

    def __str__(self):
        return self.Title
