from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('drinkers/', views.drinkers, name='drinkers'),
    path('drinkers/details/<int:id>', views.details, name='details'),
]