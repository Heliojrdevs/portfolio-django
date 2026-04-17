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