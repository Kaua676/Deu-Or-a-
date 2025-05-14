from django.urls import path
from .views import calcular_orcamento

urlpatterns = [
    path('calcular/', calcular_orcamento, name='calcular_orcamento'),
]
