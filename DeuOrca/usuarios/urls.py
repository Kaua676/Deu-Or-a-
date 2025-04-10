# usuarios/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Telas HTML
    path('cadastrar/', views.tela_cadastro, name='cadastrar_usuario'),
    path('login/', views.tela_login, name='login_usuario'),

    # APIs
    path('api/cadastrar/', views.api_cadastrar_usuario),
    path('api/login/', views.api_login_usuario),
    path('api/recuperar_senha/', views.api_recuperar_senha),
]
