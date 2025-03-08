from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    return render(request,'index.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactMessage
from django.core.mail import send_mail
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = "New Booking Request"
        message = f"""
        🚗 New Booking Request 🚗

        🔹 name: {name}
        🔹 email: {email}
        🔹 Phone: {phone}
        🔹 Message: {message}

        Please respond as soon as possible.
        """
        
        host_email = "jkkurupp26@gmail.com"  # Replace with your Gmail (Sender)
        admin_email = "vichithrandeeptham@gmail.com"    # Replace with Admin's email (Receiver)

        try:
            send_mail(subject, message, host_email, [admin_email])
            return HttpResponse("✅ Booking request sent successfully!")
        except Exception as e:
            return HttpResponse(f"❌ Error sending email: {e}")

        if name and email and phone and message:
            # Save to database
            contact_message = ContactMessage(name=name, email=email, phone=phone, message=message)
            contact_message.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Redirect to the same page after submission
        else:
            messages.error(request, "Please fill out all fields.")

        


    return render(request, 'index.html')



from .models import Booking
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse

def booking_view(request):
    if request.method == "POST":
        pickup_location = request.POST.get("pickuplocation")
        drop_location = request.POST.get("droplocation")
        phone_number = request.POST.get("number")
        pickup_time = request.POST.get("pickuptime")
        car_type = request.POST.get("cartype")

        subject = "New Booking Request"
        message = f"""
        🚗 New Booking Request 🚗

        🔹 Pickup Location: {pickup_location}
        🔹 Drop Location: {drop_location}
        🔹 Phone Number: {phone_number}
        🔹 Pickup Time: {pickup_time}
        🔹 Car Type: {car_type}

        Please respond as soon as possible.
        """
        
        host_email = "jkkurupp26@gmail.com"  
        admin_email = "vichithrandeeptham@gmail.com"   

        try:
            send_mail(subject, message, host_email, [admin_email])
            messages.success(request, "✅ Booking request sent successfully! Please check your email for confirmation.")
        except Exception as e:
            messages.error(request, f"❌ Error sending email: {e}")

        return redirect("home")  # Redirect to home page

    return render(request, "index.html")
