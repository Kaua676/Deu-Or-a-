from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('orcamentos/', include('orcamentos.urls')),
    path('calculo/', include('calculo.urls')),
    path('pdfs/', include('pdfs.urls')),
]
