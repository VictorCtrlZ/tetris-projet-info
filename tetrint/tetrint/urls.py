#~/ProjetDev/django-web-app/tetrint/listings/views.py

from django.contrib import admin
from django.urls import path

from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
    path('solo/', views.solo, name='modeSolo'),
    path('duel/', views.duel, name='modeDuel'),
    path('collaboratif/', views.collaboratif , name='modeCollaboratif'),
    path('regles/', views.regles, name='regles'),
    path('aboutus/', views.aboutus),
]
