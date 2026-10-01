#~/ProjetDev/django-web-app/tetrint/listings/views.py

from django.contrib import admin
from django.urls import path

from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('scoreboard/', views.scoreboard),
    path('solo/', views.solo, name='modeSolo'),
    path('duel/', views.duel, name='modeDuel'),
    path('collaboratif/', views.collaboratif , name='modeCollaboratif'),
    path('readme/', views.readme),
    path('aboutus/', views.aboutus),
]
