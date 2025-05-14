from django.urls import path
from .views import RegistroView, CustomLoginView, CustomLogoutView, profile

urlpatterns = [
    path('registrar/', RegistroView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('perfil/', profile, name='profile'),
]
