from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_proyectos, name='mostrar_proyectos'),
]

