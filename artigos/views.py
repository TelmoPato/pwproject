from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comen, Rating
from .forms import CommentForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import PostForm
from django.contrib.auth.models import User  # Importe o modelo de usuário

# Views para o modelo Post

def delete_comment(request, comment_id):
    # Verifique se o usuário está autenticado
    if request.user.is_authenticated:
        # Obtenha o comentário a ser excluído ou retorne um erro 404 se não existir
        comment = get_object_or_404(Comen, id=comment_id)

        # Verifique se o usuário tem permissão para excluir o comentário (se necessário)
        # Isso pode depender da sua lógica de permissão

        # Exclua o comentário
        comment.delete()

        # Redirecione de volta para a página de detalhes do post ou para onde desejar
        return redirect('artigos:post_detail', pk=comment.post.pk)
    else:
        # Se o usuário não estiver autenticado, redirecione para a página de login ou faça o que for apropriado para o seu aplicativo
        return redirect('artigos:login')



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'artigos/post_list.html', {'posts': posts})


def logout_view(request):
    logout(request)
    return redirect('artigos:post_list')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('artigos:post_list')
        else:
            mensagem = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, 'artigos/login.html', {'mensagem': mensagem})
    return render(request, 'artigos/login.html')


def delete_post(request, post_id):
    # Verifica se o usuário está autenticado
    if request.user.is_authenticated:
        # Obtém o objeto do post ou retorna um erro 404 se não existir
        post = get_object_or_404(Post, id=post_id)

        # Verifica se o método da solicitação é POST (para evitar exclusões acidentais)
        if request.method == 'POST':
            # Deleta o post
            post.delete()
            # Redireciona de volta para a lista de posts após a exclusão
            return redirect('artigos:post_list')

    else:
        # Se o usuário não estiver autenticado, redireciona para a página de login
        return redirect('artigos:login')



def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('artigos:post_list')
    else:
        form = PostForm()
    return render(request, 'artigos/add_post.html', {'form': form})





def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'artigos/post_detail.html', {'post': post})

# Views para o modelo Comen (Comentário)
def comment_list(request, post_id):
    comments = Comen.objects.filter(post_id=post_id)
    post = Post.objects.get(pk=post_id)  # Adicione esta linha para obter o objeto de postagem
    return render(request, 'artigos/comment_list.html', {'comments': comments, 'post': post})  # Adicione 'post' ao contexto


# View para criar um novo comentário
def add_comment(request, post_id):
    # Obtenha o post correspondente ao post_id
    post = get_object_or_404(Post, pk=post_id)

    # Verifique se a requisição é POST
    if request.method == 'POST':
        # Crie um formulário de comentário com os dados da requisição
        form = CommentForm(request.POST)
        if form.is_valid():
            # Salve o comentário no banco de dados
            comment = form.save(commit=False)
            comment.post = post  # Associe o comentário ao post
            comment.save()
            # Redirecione para a página de detalhes do post
            return redirect('artigos:post_detail', pk=post_id)
    else:
        # Se a requisição não for POST, crie um formulário vazio
        form = CommentForm()

    # Renderize o template para adicionar comentário
    return render(request, 'artigos/add_comment.html', {'form': form})

# Views para o modelo Rating
def post_ratings(request, post_id):
    ratings = Rating.objects.filter(post_id=post_id)
    return render(request, 'artigos/post_ratings.html', {'ratings': ratings})





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
            return render(request, 'artigos/registo.html', {'error': 'Por favor, preencha todos os campos.'})

        # Verifique se o nome de usuário já está em uso
        if User.objects.filter(username=username).exists():
            return render(request, 'artigos/registo.html', {'error': 'Nome de usuário já em uso. Por favor, escolha outro.'})

        # Crie o novo usuário
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)

        # Redirecione para a página de login após o registro bem-sucedido
        return redirect('artigos:login')

    # Se for uma solicitação GET, exiba o formulário de registro
    return render(request, 'artigos/registo.html')


