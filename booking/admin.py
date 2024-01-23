from django.contrib import admin
from .models import Table,Menu,Booking

# Register your models here.
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Menu)

