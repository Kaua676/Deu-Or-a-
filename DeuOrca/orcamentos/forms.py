from django import forms
from .models import Orcamento

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['cliente','descricao','valor','desconto','imposto']
