from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Car, ServiceHistory, UserProfile
from .forms import CarForm, UserRegistrationForm

def signup_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            UserProfile.objects.create(user=user)  # Automatically create user profile
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials!")
            return redirect("login")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")

@login_required
def dashboard(request):
    user = request.user
    user_car = Car.objects.filter(user=user).first()
    user_services = ServiceHistory.objects.filter(car=user_car) if user_car else None

    return render(request, "dashboard.html", {
        "user_car": user_car,
        "user_services": user_services,
    })

@login_required
def add_car(request):
    if Car.objects.filter(user=request.user).exists():
        messages.error(request, "You can only add one car!")
        return redirect("dashboard")

    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            messages.success(request, "Car added successfully!")
            return redirect("dashboard")
    else:
        form = CarForm()

    return render(request, "add_car.html", {"form": form})

@login_required
def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, user=request.user)

    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car details updated successfully!")
            return redirect("dashboard")
    else:
        form = CarForm(instance=car)

    return render(request, "update_car.html", {"form": form})

@login_required
def service_history(request):
    user_car = Car.objects.filter(user=request.user).first()
    if not user_car:
        messages.error(request, "You need to add a car first!")
        return redirect("dashboard")

    user_services = ServiceHistory.objects.filter(car=user_car)
    return render(request, "service_history.html", {"user_services": user_services})
