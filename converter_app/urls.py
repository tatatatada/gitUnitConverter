from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('length/', views.length_converter, name='length'),
    path('match/', views.match_game, name='match')
]

