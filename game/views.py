from django.http.response import JsonResponse
from django.shortcuts import render
from .engine import Tetris

game = Tetris()

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

def regles(request):
    return render(request, "game/regles.html")

def aboutus(request):
    return render(request, "game/aboutus.html")

def scoreboard(request):
    return render(request, "game/scoreboard.html")


def board(request):
    return JsonResponse(game.toDict())

def left(request):
    game.left()
    return JsonResponse({
        "cells": game.cells
    })

def right(request):
    game.right()
    return JsonResponse({
        "cells": game.cells
    })


def rotate(request):
    game.rotation()
    return JsonResponse({
        "cells": game.cells
    })

def update(request):
    game.tick(50)
    return JsonResponse(game.toDict())