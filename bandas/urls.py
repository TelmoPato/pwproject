from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'bandas'

urlpatterns = [
    path('', views.lista_bandas_view, name='lista_bandas'),
    path('banda/<str:banda_nome>/', views.banda_view, name='banda'),
    path('album/<str:album_titulo>/', views.album_view, name='album'),
    path('musica/<str:musica_titulo>/', views.musica_view, name='musica'),
    path('registo/', views.registo_view, name='registo'),
    path('nova_banda/', views.nova_banda_view, name='nova_banda'),
    path('lista_bandas_sbotao/', views.lista_bandas_sbotao_view, name='lista_bandas_sbotao'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recuperar_password/', views.recuperar_password_view, name='recuperar_password'),
    path('apagar_banda/<int:banda_id>/', views.apagar_banda_view, name='apagar_banda'),  # URL para apagar banda
    path('novo_album/', views.novo_album_view, name='novo_album'),
    path('bandas/banda/<str:banda_nome>/novo_album/', views.novo_album_view, name='novo_album'),
    path('bandas/album/<str:album_titulo>/apagar/', views.apagar_album, name='apagar_album'),

    path('album/<str:album_titulo>/nova_musica/', views.nova_musica_view, name='nova_musica'),
    path('musica/<str:musica_nome>/apagar/', views.apagar_musica_view, name='apagar_musica'),
    path('recuperar-senha/', auth_views.PasswordResetView.as_view(template_name='bandas/recuperar_senha.html'), name='recuperar_senha'),
    path('recuperar-senha/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='bandas/senha_reset_enviada.html'), name='password_reset_done'),
    path('recuperar-senha/confirmar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='bandas/senha_reset_confirmar.html'), name='password_reset_confirm'),
    path('recuperar-senha/concluido/', auth_views.PasswordResetCompleteView.as_view(template_name='bandas/senha_reset_concluida.html'), name='password_reset_complete'),

]

