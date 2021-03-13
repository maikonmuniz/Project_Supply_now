from .models import PRODUTO
from .forms import formsProdutos
from django.shortcuts import get_object_or_404, redirect, render

def listar_produtos(request):
    produtos = PRODUTO.objects.all()
    return render(request, 'home.html', {'produtos': produtos})

def cadastrar_produtos(request):
    form = formsProdutos()
    if request.method == "POST":
        form = formsProdutos(request.POST)

        if form.is_valid():
            

            nome = form.cleaned_data['nome']
            foto = form.cleaned_data['photo_prod']
            descricao = form.cleaned_data['descricao']
            preco = form.cleaned_data['preco']
            user = form.cleaned_data['user']
            status = form.cleaned_data['status']

            
            new_produto = PRODUTO(nome, descricao, foto, preco, user, status)
            new_produto.save()
            return redirect('listaProd')

    else:

        form = formsProdutos()
        return render(request, 'produtos/produtos_cadastro.html', {'form': form})

def lista_prod_empre(request):
    produtos = PRODUTO.objects.all()
    return render(request, 'produtos/lista_produtos_empresa.html',   {'produtos': produtos})

def edit_cadastro(request, id):
    produto = get_object_or_404(PRODUTO, id)
    form = formsProdutos(instance=produto)

    if(request.method == 'POST'):
        return False

    else:
        return render(request, 'produtos/edit_produto.html', {'form': form, 'produto': produto})


