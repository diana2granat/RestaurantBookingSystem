from django.db import models

# Create your models here.
class Table(models.Model):
    tableid=models.IntegerField(unique=True)
    capacity=models.IntegerField()
    is_booked=models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.tableid} (Capacity: {self.capacity})"
    
class Booking(models.Model):
    date=models.DateField()
    time=models.TimeField()
    guests=models.IntegerField()
    table=models.ForeignKey(Table,on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking for {self.guests} on {self.date} at {self.time}"
    

class Menu(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name