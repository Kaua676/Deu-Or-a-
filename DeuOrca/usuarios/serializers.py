# usuarios/serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'cpf_cnpj', 'tipo_usuario', 'foto_logo', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
