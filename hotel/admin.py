from django.contrib import admin
from hotel.models import Contact

# Register your models here.

admin.site.site_header = "BurgerJoint | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

admin.site.register(Contact, ContactAdmin)