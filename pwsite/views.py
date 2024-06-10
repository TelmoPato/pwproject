# project/views.py

from django.shortcuts import render

def index_view(request):
    return render(request, "pwsite/index.html")

# Create your views here.
def sobre_view(request):
    return render(request, "pwsite/sobre.html")

def interesses_view(request):
    return render(request, "pwsite/interesses.html")