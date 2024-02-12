from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    """ a view to return the home page"""
    return render(request, "index.html")