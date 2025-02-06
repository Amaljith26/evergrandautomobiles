from django.db import models

# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10, default="Not Provided")
    message = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
    

class Booking(models.Model):
    LOCATION_CHOICES = [
        ('kollam', 'Kollam'),
        ('koyilandy', 'Koyilandy'),
        ('payyoli', 'Payyoli'),
        ('nandi', 'Nandi'),
        ('vatakara', 'Vatakara'),
        ('kozhikode', 'Kozhikode'),
        ('other', 'Other'),
    ]
    
    CAR_CHOICES = [
        ('maruti', 'Maruti'),
        ('chevrolet', 'Chevrolet'),
        ('bmw', 'BMW'),
        ('mercedes', 'Mercedes'),
        ('toyota', 'Toyota'),
        ('honda', 'Honda'),
        ('hyundai', 'Hyundai'),
        ('volkswagen', 'Volkswagen'),
        ('skoda', 'Skoda'),
    ]
    pickuplocation = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    droplocation = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    phone = models.CharField(max_length=10)
    pickuptime = models.TimeField()
    cartype = models.CharField(max_length=20, choices=CAR_CHOICES)
    
    def __str__(self):
        return f"{self.pickuplocation} to {self.droplocation} - {self.cartype}"