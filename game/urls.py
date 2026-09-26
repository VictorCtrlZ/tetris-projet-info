from django.urls import path
from . import views
from .views import TraitCreate, TraitDetail

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('solo/', views.modeSolo, name='modeSolo'),
    path('duel/', views.modeDuel, name='modeDuel'),
    path('collaboratif/', views.modeCollaboratif, name='modeCollaboratif'),
    path('trait/', TraitCreate.as_view(), name='trait-list-create'),
    path('tasks/<int:pk>/', TraitDetail.as_view(), name='trait-detail'),
]