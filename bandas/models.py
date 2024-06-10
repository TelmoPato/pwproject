from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    ano_criacao = models.IntegerField()
    nacionalidade = models.CharField(max_length=100, default='Desconhecido')
    foto = models.ImageField(upload_to='bandas/', default='bandas/default.jpg')

class Album(models.Model):
    titulo = models.CharField(max_length=100, default='Album sem nome')
    ano_lancamento = models.IntegerField()
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='album_images/', null=True, blank=True)

    def __str__(self):
        return f'Banda: {self.banda.nome}, Álbum: {self.titulo}, Ano: {self.ano_lancamento}'

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField(blank=True, null=True)
    duracao = models.CharField(max_length=100, default='???')
    letra = models.TextField(blank=True, null=True)  # Novo campo para a letra da música
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'Música: {self.titulo}, Duração: {self.duracao}, Álbum: {self.album.titulo}, Banda: {self.album.banda.nome}'



