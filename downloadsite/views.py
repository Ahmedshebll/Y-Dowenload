from django.shortcuts import render, redirect
from pytube import *


# Create your views here.

def index(request):
    return render(request, 'downloadsite/index.html')

