from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('solo/', views.modeSolo, name='modeSolo'),
    path('duel/', views.modeDuel, name='modeDuel'),
    path('collaboratif/', views.modeCollaboratif, name='modeCollaboratif'),
    path("board/",views.board, name='board'),
]