import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .utils import calcular_total

@require_POST
def calcular_orcamento(request):
    data = json.loads(request.body)
    subtotal = data.get('subtotal', 0)
    desconto = data.get('desconto', 0)
    imposto  = data.get('imposto', 0)
    total = calcular_total(subtotal, desconto, imposto)
    return JsonResponse({'total': total})
