from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('length/', views.length_converter, name='length'),
    # path('weight/', views.weight_converter, name='weight'),
    # path('temperature/', views.temperature_converter, name='temperature'),
]

