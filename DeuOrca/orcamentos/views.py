from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from .models import Orcamento

from .models import Orcamento
from .forms import OrcamentoForm
from calculo.utils import calcular_total

@method_decorator(login_required, name='dispatch')
class OrcamentoListView(ListView):
    model = Orcamento
    paginate_by = 10
    template_name = 'orcamentos/orcamento_list.html'

    def get_queryset(self):
        return Orcamento.objects.filter(criado_por=self.request.user).order_by('-criado_em')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # pré-calcula o total para cada orçamento
        for o in ctx['object_list']:
            o.total = calcular_total(o.valor, o.desconto, o.imposto)
        return ctx

@method_decorator(login_required, name='dispatch')
class OrcamentoCreateView(CreateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamentos/orcamento_form.html'
    success_url = reverse_lazy('orcamento_list')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class OrcamentoUpdateView(UpdateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'orcamentos/orcamento_form.html'
    success_url = reverse_lazy('orcamento_list')

@method_decorator(login_required, name='dispatch')
class OrcamentoDetailView(DetailView):
    model = Orcamento
    template_name = 'orcamentos/orcamento_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        o = self.object
        ctx['total'] = calcular_total(o.valor, o.desconto, o.imposto)
        return ctx

@method_decorator(login_required, name='dispatch')
class OrcamentoDeleteView(DeleteView):
    model = Orcamento
    template_name = 'orcamentos/orcamento_confirm_delete.html'
    success_url = reverse_lazy('orcamento_list')

from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from .models import Orcamento

def orcamento_pdf(request, pk):
    # 1) busca o orçamento
    orc = get_object_or_404(Orcamento.objects.select_related('criado_por'), pk=pk)

    # 2) renderiza HTML
    html_string = render_to_string('orcamentos/orcamento_pdf.html', {
        'object': orc
    })

    # 3) cria PDF
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()

    # 4) retorna como resposta
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="orcamento_{orc.id}.pdf"'
    return response