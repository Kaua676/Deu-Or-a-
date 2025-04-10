# usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# ---------- API ----------
@api_view(['POST'])
@permission_classes([AllowAny])
def api_cadastrar_usuario(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def api_login_usuario(request):
    email = request.data.get('email')
    senha = request.data.get('senha')
    user = authenticate(request, email=email, password=senha)
    if user:
        return Response({'mensagem': 'Login realizado com sucesso'}, status=status.HTTP_200_OK)
    return Response({'erro': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def api_recuperar_senha(request):
    email = request.data.get('email')
    if not User.objects.filter(email=email).exists():
        return Response({'erro': 'E-mail não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'mensagem': f'Instruções enviadas para {email}'}, status=status.HTTP_200_OK)

# ---------- TELAS ----------
def tela_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        tipo_usuario = request.POST.get('tipo_usuario')
        senha = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return render(request, 'usuarios/cadastro.html', {'erro': 'E-mail já cadastrado'})
        
        User.objects.create_user(email=email, nome=nome, cpf_cnpj=cpf_cnpj, tipo_usuario=tipo_usuario, password=senha)
        return redirect('login_usuario')
    return render(request, 'usuarios/cadastro.html')

def tela_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, email=email, password=senha)
        if user:
            login(request, user)
            return redirect('/')  # Redirecionar para a home ou dashboard
        return render(request, 'usuarios/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'usuarios/login.html')
