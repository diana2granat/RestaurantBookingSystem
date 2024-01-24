from django.shortcuts import render
from booking.forms import BookingForm
from booking.models import Booking
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from datetime import timedelta

@login_required(login_url="login") # will be only executed when logged in

def book(request):
    if request.method == "POST":
# loading the form
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_details = form.cleaned_data #getting all the details from the form
            booking_date = booking_details["date"]
            booking_time = booking_details["time"]
            booking_end_time = booking_time + timedelta(hours=1)
            # filter the bookings and check if there is an overlaping booking 
            if not isinstance(request.user, AnonymousUser):
                form.instance.user = request.user
            if booking_details ["date"] < timezone.now().date():
                messages.error(request, "You need to use the future date")
                return render(request,"book.html",{"anythingform":form})
            form.save()
        else:
            print("Error occured. Fill it again")
            return render(request,"book.html",{"anythingform":form})
    else:
        form = BookingForm()
        
    return render(request,"book.html",{"anythingform":form})


        



