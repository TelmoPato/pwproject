from cursoLei.models import Curso, Area_Cientifica, Linguagem_Programacao, Disciplina, Projeto, Docente
from django.contrib import admin
from .models import Curso, Area_Cientifica, Disciplina, Projeto, Linguagem_Programacao, Docente

admin.site.register(Curso)

admin.site.register(Area_Cientifica)

admin.site.register(Disciplina)

admin.site.register(Projeto)

admin.site.register(Linguagem_Programacao)

admin.site.register(Docente)

# Register your models here.
