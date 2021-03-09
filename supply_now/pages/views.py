from django.shortcuts import render
from .models import PRODUTO


def listar_produtos(request):
    produtos = PRODUTO.objects.all()
    return render(request, 'home.html', {'produtos': produtos})
