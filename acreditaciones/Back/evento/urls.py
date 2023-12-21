from django.contrib import admin
from django.urls import path

from evento.views import ListarEventos

urlpatterns = [
    path('listar/', ListarEventos.as_view()),

]