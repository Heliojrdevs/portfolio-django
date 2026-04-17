from django.db import models

class Pessoal(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    curso = models.CharField(max_length=150)
    periodo = models.CharField(max_length=50)
    email = models.EmailField()
    git = models.URLField()
    linked = models.URLField()
    imagem_url = models.URLField(help_text="URL de uma imagem para o perfil")

    def __str__(self):
        return self.nome