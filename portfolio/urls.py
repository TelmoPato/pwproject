from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('sites-list/', views.sites_list, name='sites_list'),
    path('about-me/', views.about_me, name='about_me'),
    path('video-django/', views.video_django, name='video_django'),
    path('video-sites/', views.video_sites, name='video_sites'),
    path('redes_sociais/', views.social_links, name='social_links'),

    path('registo/', views.registo_view, name='registo'),
    path('recuperar_password/', views.recuperar_password_view, name='recuperar_password'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Adicione mais rotas conforme necessário para suas outras páginas
]
