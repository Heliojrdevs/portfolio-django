from django.db import models

class Certificado(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class Projeto(models.Model):
    TIPO_CHOICES = (
        ('Pessoal', 'Projeto Pessoal'),
        ('Disciplina', 'Projeto de Disciplina'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    link_git = models.URLField()

    def __str__(self):
        return self.nome
    
class Pessoal(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    curso = models.CharField(max_length=150)
    periodo = models.CharField(max_length=50)
    email = models.EmailField()
    git = models.URLField()
    linked = models.URLField()
    imagem_url = models.URLField()

    def __str__(self):
        return self.nome