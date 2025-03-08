from django.contrib import admin
from .models import Car, ServiceHistory, UserProfile

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("user", "model", "car_number", "color", "date_given")
    search_fields = ("user__username", "car_number")  # Allows searching by username & car number
    list_filter = ("color", "date_given")  # Filters for color & date

@admin.register(ServiceHistory)
class ServiceHistoryAdmin(admin.ModelAdmin):
    list_display = ("car", "service_type", "service_date", "service_status")
    list_filter = ("service_status", "service_date")  # Filters for service status & date
    search_fields = ("car__car_number", "service_type")  # Allows search by car number & service type

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "address", "created_at")  # Added 'created_at' for tracking
    search_fields = ("user__username", "phone")  # Allows searching by username & phone
    list_filter = ("created_at",)  # Filter users by creation date
