from django.shortcuts import render, redirect
from django.views.generic import DetailView



# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
     return render(request, 'about.html')
