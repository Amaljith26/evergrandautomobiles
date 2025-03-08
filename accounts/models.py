from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username

class Car(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Each user can have only one car
    model = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20, unique=True)  # Ensure unique car numbers
    color = models.CharField(max_length=50)
    date_given = models.DateField()

    def save(self, *args, **kwargs):
        self.car_number = self.car_number.replace(" ", "").upper()  # Normalize before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.model} ({self.car_number})"

class ServiceHistory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=200)
    service_date = models.DateField()
    service_status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Completed", "Completed")], default="Pending")
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.car.car_number} - {self.service_type} ({self.service_status})"
