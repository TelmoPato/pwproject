from django.shortcuts import render
from .models import Regiao, Praia

def lista_praias(request):
    regioes = Regiao.objects.all()
    return render(request, 'praias/lista_praias.html', {'regioes': regioes})

def detalhes_praia(request, nome_praia):
    praia = Praia.objects.get(nome=nome_praia)
    return render(request, 'praias/detalhes_praia.html', {'praia': praia})


# Create your views here.
