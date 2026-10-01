from django.http.response import JsonResponse
from django.shortcuts import render
from .tetris import Tetris


def accueil(request):
    return render(request, "game/accueil.html")

def menu(request):
    return render(request, "game/menu.html")

def modeSolo(request):
    return render(request, "game/modeSolo.html")

def modeDuel(request):
    return render(request, "game/modeDuel.html")

def modeCollaboratif(request):
    return render(request, "game/modeCollaboratif.html")

def grid(request):
    jeu = Tetris()
    return JsonResponse(jeu.get_grid())