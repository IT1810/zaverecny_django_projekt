from django.shortcuts import render
from pruzkum_zakazniku_mobilnich_operatoru_web import *

# Create your views here.

def index(requests):
    return render(requests, 'index.html', context=None)