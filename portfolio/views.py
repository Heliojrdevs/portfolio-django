from django.shortcuts import render
from core.models import Pessoal
from .models import Certificado, Projeto

def home(request):
    pessoal = Pessoal.objects.first() 
    certificados = Certificado.objects.all()
    return render(request, 'portfolio/home.html', {'pessoal': pessoal, 'certificados': certificados})

def projetos(request):
    projetos_lista = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos_lista})

def contato(request):
    pessoal = Pessoal.objects.first()
    return render(request, 'portfolio/contato.html', {'pessoal': pessoal})