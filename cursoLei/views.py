from django.shortcuts import render
from cursoLei.models import Curso, Disciplina, Projeto
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from .forms import CursoForm
from django.contrib import messages
from .forms import DisciplinaForm

@login_required
def apagar_disciplina(request, curso_nome, disciplina_id):
    curso = get_object_or_404(Curso, nome=curso_nome)
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    curso.disciplinas.remove(disciplina)
    return redirect('cursoLei:detalhes_curso', curso_nome=curso_nome)

@login_required
def adicionar_disciplina(request, curso_nome):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save()
            curso = Curso.objects.get(nome=curso_nome)
            curso.disciplinas.add(disciplina)
            # Redirecionar de volta para a página do curso após adicionar disciplina
            return redirect('cursoLei:detalhes_curso', curso_nome=curso_nome)
    else:
        form = DisciplinaForm()
    return render(request, 'cursoLei/adicionar_disciplina.html', {'form': form, 'curso_nome': curso_nome})



def apagar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    return redirect('cursoLei:lista_cursos')



def adicionar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursoLei:lista_cursos')
        else:
            messages.error(request, 'Você precisa preencher todos os campos.')
    else:
        form = CursoForm()
    return render(request, 'cursoLei/adicionar_curso.html', {'form': form})




def lista_cursos(request):
    cursos = Curso.objects.all()
    context = {'cursos': cursos}
    return render(request, 'cursoLei/lista_cursos.html', context)

def detalhes_curso(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplinas = curso.disciplinas.all()
    context = {'curso': curso, 'disciplinas': disciplinas}
    return render(request, 'cursoLei/detalhes_curso.html', context)

def detalhes_disciplina(request, disciplina_nome):
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projetos = Projeto.objects.filter(disciplina=disciplina)
    context = {'disciplina': disciplina, 'projetos': projetos}
    return render(request, 'cursoLei/detalhes_disciplina.html', context)

def detalhes_projeto(request, projeto_nome):
    projeto = Projeto.objects.get(nome=projeto_nome)
    context = {'projeto': projeto}
    return render(request, 'cursoLei/detalhes_projeto.html', context)



def logout_view(request):
    logout(request)
    return redirect('cursoLei:lista_cursos')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cursoLei:lista_cursos')
        else:
            mensagem = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, 'cursoLei/login.html', {'mensagem': mensagem})
    return render(request, 'cursoLei/login.html')



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
            return render(request, 'cursoLei/registo.html', {'error': 'Por favor, preencha todos os campos.'})

        # Verifique se o nome de usuário já está em uso
        if User.objects.filter(username=username).exists():
            return render(request, 'cursoLei/registo.html', {'error': 'Nome de usuário já em uso. Por favor, escolha outro.'})

        # Crie o novo usuário
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)

        # Redirecione para a página de login após o registro bem-sucedido
        return redirect('cursoLei:login')

    # Se for uma solicitação GET, exiba o formulário de registro
    return render(request, 'cursoLei/registo.html')

# Create your views here.
