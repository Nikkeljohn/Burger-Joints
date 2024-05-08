from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/',views.contact_us,name="contact"),
    path('dashboard/', views.dashboard, name='dashboard'),
]
