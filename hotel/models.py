from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="categories/%Y/%m/%d")
    icon = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team")
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # facebook_url = models.CharField(blank=True,max_length=200)
    # twitter_url = models.CharField(blank=True,max_length=200)

    def __str__(self):
        return self.name 

class Dish(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='dishes/%Y/%m/%d')
    ingredients = models.TextField()
    details = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discounted_price = models.FloatField(blank=True)
    is_available = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural ="Dish Table"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/%Y/%m/%d', null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural="Profile Table"

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Dish, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    invoice_id = models.CharField(max_length=100, blank=True)
    payer_id = models.CharField(max_length=100, blank=True)
    ordered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.user.first_name

    class Meta:
        verbose_name_plural = "Order Table"
 
TIME_BOOKING = ((1, "4:00pm - 5:00pm" ),(2,"5:00pm _ 6:00pm"),
                (3,"6:00pm - 7:00pm"),(4,"7:00pm - 8:00pm"),
                (5,"8:00pm - 9:00pm"),(6,"9:00 - 10:00pm"))

SEATINGS = ((2, "2"),(4, "4"), (6, "6"), (8, "8"), (10, "10"), (12, "12"))

class Table(models.Model):
    """ Model to create Tables """
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField(choices=SEATINGS, default=2)
    wheelchair_accessible = models.BooleanField(default=True)

    class Meta:
        """ Order by table number """
        ordering = ['table_number']

    def __str__(self):
        return str(self.table_number)


class Booking(models.Model):
    """ Model to create a booking """
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_customer")
    booking_name = models.CharField(max_length=25)
    booked_table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="booking_table")
    number_of_guests = models.IntegerField(default=2)
    booking_date = models.DateField()
    booking_time = models.IntegerField(choices=TIME_BOOKING, default=1)

    class Meta:
        """ Order by booking_date and then booking_time """
        ordering = ['booking_date', 'booking_time']

    def __str__(self):
        return str(self.pk)
