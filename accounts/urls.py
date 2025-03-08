from django.urls import path
from . import views  # Make sure to import your views
from .views import dashboard, add_car, service_history, update_car
from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add-car/", views.add_car, name="add_car"),
    path("update-car/<int:car_id>/", views.update_car, name="update_car"),
    path("service-history/", views.service_history, name="service_history"),
]
