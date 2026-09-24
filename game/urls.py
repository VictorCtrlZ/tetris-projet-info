from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('solo/', views.mode_solo, name='modeSolo'),
    path('duel/', views.mode_duel, name='modeDuel'),
    path('collaboratif/', views.mode_collaboratif, name='modeCollaboratif'),
]