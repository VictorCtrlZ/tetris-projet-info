#~/ProjetDev/django-web-app/tetrint/listings/views.py

from django.contrib import admin
from django.urls import path

from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.menu),
    path('scoreboard/', views.scoreboard),
    path('solo/', views.solo),
    path('duel/', views.duel),
    path('readme/', views.readme),
    path('aboutus/', views.aboutus),
]
