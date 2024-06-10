from django.urls import path
from . import views
from .views import adicionar_disciplina
from django.contrib.auth import views as auth_views

app_name = 'cursoLei'

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),

    path('curso/<str:curso_nome>/', views.detalhes_curso, name='detalhes_curso'),

    path('disciplina/<str:disciplina_nome>/', views.detalhes_disciplina, name='detalhes_disciplina'),
    path('projeto/<str:projeto_nome>/', views.detalhes_projeto, name='detalhes_projeto'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),


    path('registo/', views.registo_view, name='registo'),

    path('adicionar_curso/', views.adicionar_curso, name='adicionar_curso'),

    path('curso/<int:curso_id>/apagar/', views.apagar_curso, name='apagar_curso'),

   path('adicionar-disciplina/<str:curso_nome>/', views.adicionar_disciplina, name='adicionar_disciplina'),

   path('curso/<str:curso_nome>/apagar-disciplina/<int:disciplina_id>/', views.apagar_disciplina, name='apagar_disciplina'),




    path('recuperar-senha/', auth_views.PasswordResetView.as_view(template_name='bandas/recuperar_senha.html'), name='recuperar_senha'),
    path('recuperar-senha/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='bandas/senha_reset_enviada.html'), name='password_reset_done'),
    path('recuperar-senha/confirmar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='bandas/senha_reset_confirmar.html'), name='password_reset_confirm'),
    path('recuperar-senha/concluido/', auth_views.PasswordResetCompleteView.as_view(template_name='bandas/senha_reset_concluida.html'), name='password_reset_complete'),
]