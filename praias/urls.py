from django.urls import path
from .views import lista_praias, detalhes_praia

urlpatterns = [
    path('lista-praias/', lista_praias, name='lista_praias'),
    path('detalhes-praia/<str:nome_praia>/', detalhes_praia, name='detalhes_praia'),
]
