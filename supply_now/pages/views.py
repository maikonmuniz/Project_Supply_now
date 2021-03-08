from .models import PRODUTO
from django.shortcuts import render




def listar_produtos(request):
    produtos = PRODUTO.objects.all()
    return render(request, 'home.html', {'produtos': produtos})

