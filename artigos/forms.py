from django import forms
from .models import Comen
from .models import Post
from django.forms.widgets import TextInput


class CustomDateTimeInput(TextInput):
    input_type = 'datetime-local'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'data', 'foto']
        widgets = {
            'data': CustomDateTimeInput(),  # Usa o widget personalizado para o campo data
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comen
        fields = ['nome', 'comentario']  # Defina aqui os campos do formulário de comentário



