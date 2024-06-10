from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'artigos'

urlpatterns = [
    # URLs para o modelo Post

    path('add_post/', views.add_post, name='add_post'),


    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),

    # URLs para o modelo Comen (Comentário)
    path('<post_id>/comentarios/', views.comment_list, name='comment_list'),

    # Se desejar uma URL para criar um comentário
    # path('<post_id>/comentarios/criar/', views.comment_create, name='comment_create'),

    # URLs para o modelo Rating
    path('<post_id>/ratings/', views.post_ratings, name='post_ratings'),

    path('<int:post_id>/add_comment/', views.add_comment, name='add_comment'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),



    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),

     path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),


     path('registo/', views.registo_view, name='registo'),



    path('recuperar-senha/', auth_views.PasswordResetView.as_view(template_name='bandas/recuperar_senha.html'), name='recuperar_senha'),
    path('recuperar-senha/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='bandas/senha_reset_enviada.html'), name='password_reset_done'),
    path('recuperar-senha/confirmar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='bandas/senha_reset_confirmar.html'), name='password_reset_confirm'),
    path('recuperar-senha/concluido/', auth_views.PasswordResetCompleteView.as_view(template_name='bandas/senha_reset_concluida.html'), name='password_reset_complete'),


]


