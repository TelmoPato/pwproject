# urls.py

from django.contrib import admin
from django.urls import path, include   # incluir include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bandas/', include('bandas.urls')),
    path('noobsite/', include('noobsite.urls')),  # novo path
    path('pwsite/', include('pwsite.urls')),  # novo path
    path('artigos/', include('artigos.urls')),
    path('cursoLei/', include('cursoLei.urls')),
    path('praias/', include('praias.urls')),
    path('meteo/', include('meteo.urls')),
    path('', include('portfolio.urls')),


]
