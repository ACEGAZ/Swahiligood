from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    """ a view to return the home page"""
    return render(request, "index.html")

def menu(request):
    """ a view to return the menu page"""
    return render(request, "menu.html")

def about_us(request):
    """ a view to return the about_us page"""
    return render(request, "about_us.html")