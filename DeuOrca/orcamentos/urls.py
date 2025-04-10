# orcamentos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario_orcamento, name='formulario_orcamento'),
]
