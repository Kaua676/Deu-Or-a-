from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views import View
from .forms import RegistroForm

class RegistroView(View):
    def get(self, request):
        return render(request, 'usuarios/register.html', {'form': RegistroForm()})
    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('orcamento_list')
        return render(request, 'usuarios/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'

def profile(request):
    return render(request, 'usuarios/profile.html')
