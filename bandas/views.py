from .models import Banda, Album, Musica
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import BandaForm
from .forms import AlbumForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MusicaForm

from django.shortcuts import get_object_or_404, redirect



@login_required
def nova_banda_view(request):
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES)  # Adicione request.FILES aqui
        if form.is_valid():
            form.save()
            return redirect('bandas:lista_bandas')
    else:
        form = BandaForm()
    return render(request, 'bandas/nova_banda.html', {'form': form})

def apagar_musica_view(request, musica_nome):
    musica = get_object_or_404(Musica, titulo=musica_nome)
    if request.method == 'POST':
        album_titulo = musica.album.titulo
        musica.delete()
        return redirect('bandas:album', album_titulo=album_titulo)
    return redirect('bandas:album', album_titulo=musica.album.titulo)


def apagar_album(request, album_titulo):
    album = get_object_or_404(Album, titulo=album_titulo)
    if request.method == 'POST':
        banda_nome = album.banda.nome
        album.delete()
        return redirect('bandas:banda', banda_nome=banda_nome)
    return redirect('bandas:banda', banda_nome=album.banda.nome)


@login_required
def novo_album_view(request, banda_nome):
    banda = get_object_or_404(Banda, nome=banda_nome)

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.banda = banda
            album.save()
            return redirect('bandas:banda', banda_nome=banda_nome)
    else:
        form = AlbumForm()

    return render(request, 'bandas/novo_album.html', {'form': form})



@login_required
def nova_musica_view(request, album_titulo):
    album = get_object_or_404(Album, titulo=album_titulo)

    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.album = album
            musica.save()
            return redirect('bandas:album', album_titulo=album_titulo)
    else:
        form = MusicaForm()

    return render(request, 'bandas/nova_musica.html', {'form': form})



def banda_view(request, banda_nome):

    banda_nome = banda_nome.replace('-', ' ').title()


    banda = Banda.objects.get(nome=banda_nome)
    albuns = Album.objects.filter(banda=banda)
    context = {
        'banda': banda,
        'albuns': albuns,
    }
    return render(request, 'bandas/banda.html', context)






def album_view(request, album_titulo):
    album = Album.objects.get(titulo=album_titulo)
    musicas = Musica.objects.filter(album=album)
    context = {
        'album': album,
        'musicas': musicas,
    }
    return render(request, 'bandas/album.html', context)

def musica_view(request, musica_titulo):
    musica = Musica.objects.get(titulo=musica_titulo)
    context = {
        'musica': musica,
    }
    return render(request, 'bandas/musica.html', context)

def lista_bandas_view(request):
    bandas = Banda.objects.all()
    context = {
        'bandas': bandas,
    }
    return render(request, 'bandas/lista_bandas.html', context)


@login_required
def apagar_banda_view(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)

    # Exclui a banda
    banda.delete()

    # Redireciona de volta para a página de lista de bandas
    return redirect('bandas:lista_bandas')



def registo_view(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        # Verifique se todos os campos foram preenchidos
        if not (username and email and first_name and last_name and password):
            return render(request, 'bandas/registo.html', {'error': 'Por favor, preencha todos os campos.'})

        # Verifique se o nome de usuário já está em uso
        if User.objects.filter(username=username).exists():
            return render(request, 'bandas/registo.html', {'error': 'Nome de usuário já em uso. Por favor, escolha outro.'})

        # Crie o novo usuário
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)

        # Redirecione para a página de login após o registro bem-sucedido
        return redirect('bandas:login')

    # Se for uma solicitação GET, exiba o formulário de registro
    return render(request, 'bandas/registo.html')


def lista_bandas_sbotao_view(request):
    bandas = Banda.objects.all()
    return render(request, 'bandas/lista_bandas_sbotao.html', {'bandas': bandas})



def recuperar_password_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        nova_password = request.POST.get('nova_password')

        # Verifica se o usuário com o username fornecido existe
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Se o usuário não existe, mostra uma mensagem de erro
            return render(request, 'bandas/recuperar_password.html', {'error': 'Username não encontrado.'})

        # Atualiza a password do usuário com a nova password fornecida
        user.set_password(nova_password)
        user.save()

        # Redireciona para a página de login após a recuperação bem-sucedida
        return redirect('bandas:login')

    return render(request, 'bandas/recuperar_password.html')


def logout_view(request):
    logout(request)
    return redirect('bandas:lista_bandas')



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bandas:lista_bandas')
        else:
            mensagem = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, 'bandas/login.html', {'mensagem': mensagem})
    return render(request, 'bandas/login.html')


@login_required
def nova_banda_view(request):
    if request.method == 'POST':
        form = BandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bandas:lista_bandas')
    else:
        form = BandaForm()
    return render(request, 'bandas/nova_banda.html', {'form': form})


# Create your views here.
