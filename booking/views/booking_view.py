from django.shortcuts import render
from booking.forms import BookingForm
from booking.models import Booking
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required(login_url="login") # will be only executed when logged in

def book(request):
    if request.method == "POST":
# loading the form
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_details = form.cleaned_data #getting all the details from the form
            form.save()
            if booking_details ["date"] < timezone.now().date():
                print("You need to use the future date")   #we have to add here something
                return render(request,"book.html",{"anythingform":form})
        else:
            print("Error occured. Fill it again")
            return render(request,"book.html",{"anythingform":form})
    else:
        form = BookingForm()
        
    return render(request,"book.html",{"anythingform":form})


        



