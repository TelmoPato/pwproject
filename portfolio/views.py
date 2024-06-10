# No arquivo views.py da sua aplicação portfolio

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def landing_page(request):
    return render(request, 'portfolio/landing_page.html')

def sites_list(request):
    return render(request, 'portfolio/sites_list.html')

def about_me(request):
    return render(request, 'portfolio/about_me.html')

def video_django(request):
    return render(request, 'portfolio/video_django.html')

def video_sites(request):
    return render(request, 'portfolio/video_sites.html')

def social_links(request):  # Nova view
    return render(request, 'portfolio/social_links.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')  # Redirecionar para a página inicial do portfólio
        else:
            return render(request, 'portfolio/login.html', {'mensagem': 'Credenciais inválidas'})
    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)
    return redirect('landing_page')  # Redireciona para a landing page



def registo_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        login(request, user)
        return redirect('portfolio:landing_page')

    return render(request, 'portfolio/registo.html')

def recuperar_password_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nova_password = request.POST.get('nova_password')
        try:
            user = User.objects.get(username=username)
            user.set_password(nova_password)
            user.save()
            messages.success(request, 'Password alterada com sucesso!')
            return redirect('portfolio:login')
        except User.DoesNotExist:
            messages.error(request, 'Usuário não encontrado')

    return render(request, 'portfolio/recuperar_password.html')
