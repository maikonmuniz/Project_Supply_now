from django.db import models
from django.contrib.auth.models import User

Status = (
    ("Sim", "Temos em Estoque"),
    ("Não", "Não temos em Estoque"),
)


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    telefone = models.CharField(max_length=12)  # existe PhoneNumberField
    email = models.EmailField(max_length=25)
    rua = models.CharField(max_length=40)
    cidade = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    horario_entrega = models.CharField(max_length=25)
    foto_empresa = models.ImageField(upload_to="img/%Y")


class Produto(models.Model):
    empresa = models.ForeignKey(Empresa,
                                on_delete=models.CASCADE,
                                related_name="produtos")
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    photo_prod = models.ImageField(upload_to="img/%y")
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50,
        choices=Status,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
