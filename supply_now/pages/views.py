from django.shortcuts import render
from .models import Produto


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos})
