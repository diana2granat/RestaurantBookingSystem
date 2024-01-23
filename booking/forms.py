from django import forms
from .models import Booking


class BookingForm (forms.ModelForm):
    phone = forms.IntegerField(required=True)
    class Meta:
        model = Booking
        fields = ["date", "time", "guests","phone"]
        widgets = {
            "date": forms.DateInput(attrs = {"type":"date"}),
            "time": forms.TimeInput(attrs = {"type":"time"})
        }
