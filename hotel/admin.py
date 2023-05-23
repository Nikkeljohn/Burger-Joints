from django.contrib import admin
from hotel.models import Contact, Category, Team, Dish, Profile, Order, Booking

admin.site.site_header = "FoodZone | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class DishAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','added_on','updated_on']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'date', 'time', 'guest','added_on','is_approved']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Team, TeamAdmin )
admin.site.register(Dish, DishAdmin )
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Booking, BookingAdmin)
