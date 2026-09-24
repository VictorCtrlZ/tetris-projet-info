#~/ProjetDev/django-web-app/tetrint/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

def menu(request):
    return render(request, 'menu.html')

def scoreboard(request):
    return render(request, 'scoreboard.html')

def solo(request):
    return render(request, 'solo.html')

def duel(request):
    return render(request, 'duel.html')

def readme(request):
    return render(request, 'readme.html')

def aboutus(request):
    return render(request, 'aboutus.html')