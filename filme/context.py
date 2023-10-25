from .models import Filme

#Lista de Filmes mais recentes
def lista_filmes_frequentes(request):
    lista_filmes = Filme.objects.all().order_by("-data_criacao")[0:10]
    return {"lista_filmes_recentes": lista_filmes}


# Lista de Filmes em alta
def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by("-visualizacoes")[0:10]
    return {"lista_filmes_emalta": lista_filmes}