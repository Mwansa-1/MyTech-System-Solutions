from django.shortcuts import render , redirect ,get_object_or_404
from . import forms
from django.http import HttpResponse
from .models import Booking , Testimonial , Team , TeamOnSite
from django.conf.urls.static import static


## views for the pages 
def index(request):
    if request.method == 'POST':
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('index')  # Redirect to a different page after successful form submission
    else:
        form = forms.BookingForm()

    return render(request, "mts_profile/index.html", {
        "testimonials" : Testimonial.objects.all(),
        "team" : Team.objects.all(),
        "form": form
    })

    

    

def team(request):
    return render(request, 'mts_profile/team.html',{
        "teamOnSite" : TeamOnSite.objects.all()
    })

def services(request):
    if request.method == 'POST':
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('services')  # Redirect to a different page after successful form submission
    else:
        form = forms.BookingForm()

    return render(request, "mts_profile/services.html", {
        "testimonials" : Testimonial.objects.all(),
        "form": form
    })

def contact(request):
    if request.method == 'POST':
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('contact')  # Redirect to a different page after successful form submission
    else:
        form = forms.BookingForm()

    return render(request, "mts_profile/contact.html", {
        "testimonials" : Testimonial.objects.all(),
        "form": form
    })

## book form view
