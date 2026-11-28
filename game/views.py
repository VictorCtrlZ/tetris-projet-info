from django.http.response import JsonResponse
from django.shortcuts import render, redirect

from .engine import Tetris
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

game = Tetris()

def accueil(request):
    return render(request, "game/accueil.html")

@login_required(login_url="connexion")
def menu(request):
    global game
    game = Tetris()
    return render(request, "game/menu.html")

@login_required(login_url="connexion")
def modeSolo(request):
    return render(request, "game/modeSolo.html")

@login_required(login_url="connexion")
def modeDuel(request):
    return render(request, "game/modeDuel.html")

@login_required(login_url="connexion")
def modeCollaboratif(request):
    return render(request, "game/modeCollaboratif.html")

@login_required(login_url="connexion")
def scoreboard(request):
    return render(request, "game/scoreboard.html")

def erreur404(request):
    return render(request, '404.html')

def inscription(request):
    return render(request, "game/inscription.html")

def connexion(request):
    return render(request, "game/connexion.html")


def board(request):
    return JsonResponse(game.toDict())

def left(request):
    game.left()
    return JsonResponse(game.toDict())


def right(request):
    game.right()
    return JsonResponse(game.toDict())


def rotate(request):
    game.rotation()
    return JsonResponse(game.toDict())

def update(request):
    game.tick(50)
    return JsonResponse(game.toDict())

def fastFall(request):
    game.setFastFall(request.GET.get("on") == "true")
    return JsonResponse(game.toDict())


def restart(request):
    global game
    game = Tetris()
    return JsonResponse(game.toDict())

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Login incorrect")
            return redirect("game/connexion.html")

        user = authenticate(request, username = username, password = password)
        if user is None:
            messages.error(request, "Mot de passe incorrect")
            return redirect("connexion")
        else:
            login(request, user)
            return redirect("menu")
    return render(request, "game/connexion.html")


def inscriptionPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Nom déjà utilisé")
            return redirect("inscription")

        user=User.objects.create_user(username = username, password = password)
        user.set_password(password)
        user.save()

        messages.info(request, "Compte créé")
        return redirect("inscription")
    return render(request, "game/inscription.html")



def logoutPage(request):
    logout(request)
    return redirect("connexion")
