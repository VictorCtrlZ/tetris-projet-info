"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path


urlpatterns = [
    path('', RedirectView.as_view(url='/accueil/', permanent=True)), #Permet la re-direction des requêtes à la racine vers le /accueil
    path('admin/', admin.site.urls),
    path('api/', include('game.urls')),
    path('accueil/', views.accueil, name='accueil'),
    path('menu/', views.menu, name='menu'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
    path('solo/', views.solo, name='modeSolo'),
    path('duel/', views.duel, name='modeDuel'),
    path('collaboratif/', views.collaboratif , name='modeCollaboratif'),
    path('regles/', views.regles, name='regles'),
    path('404/', views.erreur404, name='404'),
    path('aboutus/', views.aboutus)
]

