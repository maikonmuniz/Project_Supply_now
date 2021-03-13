from django import forms
from .models import PRODUTO


class formsProdutos(forms.ModelForm):

    class Meta:
        model = PRODUTO
        fields = ('nome','descricao',  'photo_prod', 'preco', 'user', 'status')