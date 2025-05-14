from django.db import models
from django.contrib.auth.models import User

class Orcamento(models.Model):
    cliente = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imposto  = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # %
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cliente} – R$ {self.valor}'
