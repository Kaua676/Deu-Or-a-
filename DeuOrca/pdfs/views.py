from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from orcamentos.models import Orcamento
from calculo.utils import calcular_total

def orcamento_pdf(request, pk):
    o = Orcamento.objects.get(pk=pk, criado_por=request.user)
    template = get_template('pdfs/orcamento_pdf.html')
    total = calcular_total(o.valor, o.desconto, o.imposto)
    html = template.render({'orcamento': o, 'total': total})
    resp = HttpResponse(content_type='application/pdf')
    resp['Content-Disposition'] = f'attachment; filename="orcamento_{pk}.pdf"'
    pisa.CreatePDF(html, dest=resp)
    return resp
