from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory, name='inventory-home'),
    path('about/', views.about, name='inventory-about'),
]