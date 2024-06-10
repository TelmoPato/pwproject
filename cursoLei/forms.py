from django import forms
from .models import Curso, Disciplina
from .models import Disciplina

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'ano', 'semestre', 'ects', 'code', 'conteudos', 'area_cientifica']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'apresentacao', 'objetivos', 'competencias', 'disciplinas']
        labels = {
            'nome': 'Nome',
            'apresentacao': 'Apresentação',
            'objetivos': 'Objetivos',
            'competencias': 'Competências',
            'disciplinas': 'Disciplinas',
        }