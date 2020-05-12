from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def register(request):
    return render(request,'core/register.html')

def login(request):
    return render(request,'core/login.html')

def about(request):
    return render(request,'core/about.html')

def menu(request):
    return render(request,'core/menu.html')

def reservation(request):
    return render(request,'core/reservation.html')

def gallery(request):
    return render(request,'core/gallery.html')

def review(request):
    return render(request,'core/review.html')

def blog(request):
    return render(request,'core/blog.html')