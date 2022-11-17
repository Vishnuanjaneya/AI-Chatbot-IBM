from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def index(request):
    return render(request,'index.html')

def products(request):
    return render(request, 'products.html')

def contacts(request):
    return render(request, 'contacts.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

