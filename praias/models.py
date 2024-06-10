from django.db import models

class Regiao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=50)  # Alteração aqui
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Praia(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    servicos_disponiveis = models.ManyToManyField(Servico)
    foto = models.ImageField(upload_to='praia_images/', null=True, blank=True)

    def __str__(self):
        return f'Praia: {self.nome}, Região: {self.regiao.nome}'
