from django import forms
from .models import Banda, Album, Musica

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'ano', 'duracao', 'letra', 'album']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'ano_lancamento', 'imagem']  # Adicione 'imagem' aos campos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagem'].widget.attrs.update({'class': 'form-control-file'})

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nome', 'ano_criacao', 'nacionalidade']


