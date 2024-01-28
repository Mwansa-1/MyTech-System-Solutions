from django import forms
from . import models

class BookingForm(forms.ModelForm):
    SERVICE_CHOICES = [
        ('choose', ' Choose Your Service'),
        ('StarLink Installation', 'StarLink Installation'),
        ('IT Consulting', 'IT Consulting'),
        ('Managed IT Services', 'Managed IT Services'),
        ('StarLink Installation', 'StarLink Installation'),
        ('Network Design and Implementation', 'Network Design and Implementation'),
        ('CCTV Installation', 'CCTV Installation'),
        ('Access Door Installation', 'Access Door Installation'),
        ('Cyber Security Services', 'Cyber Security Services'), 
        ('Cloud Computing Services', 'Cloud Computing Services'),
        ('Software Development', 'Software Development'),
        ('Hardware Procurement', 'Hardware Procurement'),
        ('Data Backup and Recovery', 'Data Backup and Recovery'),
        ('VoIP and Unified Communications', 'VoIP and Unified Communications'),
        ('IT Training and Support', 'IT Training and Support'),
        ('Other', 'Other'),
        # Add more choices as needed
    ]

    # Modify the service field to use TypedChoiceField with the choices
    service = forms.TypedChoiceField(choices=SERVICE_CHOICES,)

    class Meta : 
        model = models.Booking
        fields = ['full_name','phone_number', 'email', 'service', 'location' , 'message', 'date', 'time']