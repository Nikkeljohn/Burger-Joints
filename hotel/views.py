from django.shortcuts import render
from hotel.models import Contact
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact_us(request):
    context={}
    if request.method=="POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")
        
        obj = Contact(name=name, email=em, subject=sub, message=msz)
        obj.save()
        context['message']=f"Dear {name}, Your Mesage has been sent!"
        
   
    return render(request,'contact.html', context)

def booking(request):
    return render(request, 'booking.html')

def about(request):
    return render(request, 'about.html')
