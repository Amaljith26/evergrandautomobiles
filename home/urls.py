from django.urls import path
from . import views  # Make sure to import your views

urlpatterns = [
    path('', views.home, name='home'),
    path('Contact/', views.contact_view, name='contact'),
    path("booking/", views.booking_view, name="booking"),
 # Provide the view function here
]