from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=1000)
    data = models.DateTimeField(verbose_name="Data de Publicação")  # Alteração feita aqui
    foto = models.ImageField()

    def __str__(self):
        return f'Titulo: {self.titulo}'

class Comen(models.Model):
    nome = models.CharField(max_length=300)
    comentario = models.CharField(max_length=30000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



class Rating(models.Model):
    valor = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Rating: {self.valor}, Artigo: {self.post.titulo}'
