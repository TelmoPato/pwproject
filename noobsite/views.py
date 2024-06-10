# project/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_view1(request):
    return HttpResponse("Teste 1")

def index_view2(request):
    return HttpResponse("Teste 2")

def index_view3(request):
    return HttpResponse("Teste 3")
