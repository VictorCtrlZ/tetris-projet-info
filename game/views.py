from django.shortcuts import render
from rest_framework import generics
from .models import Trait
from .serializers import TraitSerializer

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


class TraitCreate(generics.ListCreateAPIView):
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer

class TraitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer