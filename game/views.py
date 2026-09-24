from django.shortcuts import render

def accueil(request):
    return render(request, "game/accueil.html")

def menu(request):
    return render(request, "game/menu.html")

def mode_solo(request):
    return render(request, "game/mode_solo.html")

def mode_duel(request):
    return render(request, "game/mode_duel.html")

def mode_collaboratif(request):
    return render(request, "game/mode_collaboratif.html")