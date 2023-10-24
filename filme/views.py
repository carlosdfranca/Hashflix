from typing import Any
from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
class Homepage(TemplateView):
    template_name = "homepage.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme


class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get_context_data(self, **kwargs):
        context =  super(Detalhesfilme, self).get_context_data(**kwargs)

        # Filtrar a tabela de filmes que tenham a mesma categoria do filme selecionado
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:10]
        context['filmes_relacionados'] = filmes_relacionados
        return context



# def homepage(request):
#     return render(request, "homepage.html")

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)