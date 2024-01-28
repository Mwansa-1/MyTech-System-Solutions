from django.shortcuts import render

# Create your views here.

from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm , CustomAuthenticationForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            
            #log user in
            #log the user in
            user= form.save()
            login(request , user)
            return redirect('signupsuccessful')
    form = CustomUserCreationForm()
    return render(request , "accounts/signup.html" , {"form":form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data = request.POST)
        if form.is_valid():
            #log the user in
            user = form.get_user()
            login(request , user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('online_store')
    else:
        form = CustomAuthenticationForm()
    return render(request , "accounts/login.html" , {"form":form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('online_store')
    
def signupsuccessful(request):
    return render(request , "accounts/singupsuccessful.html")