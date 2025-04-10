from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
import io

def formulario_orcamento(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        tipo = request.POST.get('tipo')

        template = get_template('orcamentos/orcamento_pdf.html')
        html = template.render({
            'descricao': descricao,
            'valor': valor,
            'tipo': tipo
        })

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="orcamento.pdf"'
        pisa.CreatePDF(io.StringIO(html), dest=response)
        return response

    return render(request, 'orcamentos/criar_orcamento.html')
