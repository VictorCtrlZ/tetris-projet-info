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
    game.rotate()
    return JsonResponse({
        "cells": game.cells
    })
