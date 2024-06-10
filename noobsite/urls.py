# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('teste1/', views.index_view1),
    path('teste2/', views.index_view2),
    path('teste3/', views.index_view3),
]