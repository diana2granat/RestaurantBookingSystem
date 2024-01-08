from django.shortcuts import render
from booking.models import Table

def list_tables(request):
    tables = Table.objects.all()
    return render (request,"tables.html", {"tables":tables})

