from collections import namedtuple
from django.urls import path


from . import views

app_name = "pages"


urlpatterns = [
     #path('', views.HomePageView.as_view(), name='home'),
     path('', views.listar_produtos, name='home'),
     path('Produtos_Empresa', views.lista_prod_empre, name='listaProd'),
     path('Cadastro_Produtos', views.cadastrar_produtos, name='cad_prod'),
     path('editProduto/<int:id>', views.edit_cadastro, name="produto"),

    ]
