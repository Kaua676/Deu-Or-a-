from django.urls import path
from .views import (
    OrcamentoListView, OrcamentoCreateView, OrcamentoUpdateView,
    OrcamentoDetailView, OrcamentoDeleteView
)

urlpatterns = [
    path('', OrcamentoListView.as_view(), name='orcamento_list'),
    path('novo/', OrcamentoCreateView.as_view(), name='orcamento_create'),
    path('<int:pk>/', OrcamentoDetailView.as_view(), name='orcamento_detail'),
    path('<int:pk>/editar/', OrcamentoUpdateView.as_view(), name='orcamento_update'),
    path('<int:pk>/excluir/', OrcamentoDeleteView.as_view(), name='orcamento_delete'),
    path('pdf/<int:pk>/', orcamento_pdf, name='orcamento_pdf'),
]
