from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
]
