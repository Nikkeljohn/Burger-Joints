from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TIME_BOOKING = ((1, "4:00pm - 5:00pm" ),(2,"5:00pm _ 6:00pm"),
                (3,"6:00pm - 7:00pm"),(4,"7:00pm - 8:00pm"),
                (5,"8:00pm - 9:00pm"),(6,"9:00 - 10:00pm"))

SEATINGS = ((2, "2"),(4, "4"), (6, "6"), (8, "8"), (10, "10"), (12, "12"))

class Booking(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_customer")
    booking_name = model.CharField(max_length=20)
    tabel = models.ForeignKey(
        Tabel, on_delete=models.CASCADE, related_name="booking_tabel")
    guests = models.IntegerField(default=1)
    date = models.DateField()
    time = models.IntegerField(choices=TIME_BOOKING, default=1)

    class Meta:
            
        ordering = ['date', 'time']

    def __str__(self):
        return str(self.pk)  

class Tabel(models.Model):
    seat_number = models.IntegerField(unique=True)
    seatings = models.IntegerField(choices=SEATINGS, default=True)
    wheelchair_accessible = models.BooleanField(default=True)

    class Meta:
        """ Order by table number """
        ordering = ['table_number']

    def __str__(self):
        return str(self.seat_number)    