from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('solo/', views.modeSolo, name='modeSolo'),
    path('duel/', views.modeDuel, name='modeDuel'),
    path('collaboratif/', views.modeCollaboratif, name='modeCollaboratif'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
    path('regles/', views.regles, name='regles'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('board/',views.board, name='board'),
    path('rotate/',views.rotate, name='rotate'),
    path('left/',views.left, name='left'),
    path('right/',views.right, name='right'),
    path('update/',views.update, name='update')
]