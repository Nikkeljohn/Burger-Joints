from django import forms
from datetime import datetime
from .models import Booking, Table

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=15)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'Date', 'data-target': '#date', 'data-toggle': 'datetimepicker'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'Time', 'data-target': '#time', 'data-toggle': 'datetimepicker'}))
    guests = forms.ChoiceField(choices=[(i, f'{i} Guest') for i in range(1, 11)], widget=forms.Select(attrs={'class': 'custom-select form-control'}))