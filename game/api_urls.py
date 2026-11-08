from django.urls import path
from . import views

urlpatterns = [
    path('board/',views.board, name='board'),
    path('rotate/',views.rotate, name='rotate'),
    path('left/',views.left, name='left'),
    path('right/',views.right, name='right'),
    path('update/',views.update, name='update'),
    path('fastFall/',views.fastFall, name='fastFall'),
    path('restart/',views.restart, name='restart')
]