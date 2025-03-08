from django import forms
from django.contrib.auth.models import User
from .models import Car

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["model", "car_number", "color", "date_given"]
        widgets = {
            "date_given": forms.DateInput(attrs={"type": "date"})
        }

    def clean_car_number(self):
        car_number = self.cleaned_data.get("car_number")
        normalized_car_number = car_number.replace(" ", "").upper()  # Normalize input
        
        # Check if the normalized car number already exists
        if Car.objects.filter(car_number__iexact=normalized_car_number).exists():
            raise forms.ValidationError("This car number is already registered!")

        return car_number