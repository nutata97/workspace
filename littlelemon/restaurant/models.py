from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # ID field as primary key
    name = models.CharField(max_length=255)  # Name field with max length 255
    no_of_guests = models.IntegerField()  # Number of guests
    booking_date = models.DateTimeField()  # Booking date and time

    def __str__(self):
        return f"{self.name} - {self.booking_date}"
    
class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # ID field as primary key
    title = models.CharField(max_length=255)  # Title field with max length 255
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price field with 2 decimal places
    inventory = models.IntegerField()  # Inventory field

    def __str__(self):
        return f"{self.title} - ${self.price}"