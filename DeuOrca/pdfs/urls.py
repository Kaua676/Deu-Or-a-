from django.urls import path
from .views import orcamento_pdf

urlpatterns = [
    path('<int:pk>/', orcamento_pdf, name='orcamento_pdf'),
]
