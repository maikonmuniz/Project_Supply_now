from django.db import models
from django.contrib.auth.models import User

Status = (
    ("Sim", "Temos em Estoque"),
    ("Não", "Não temos em Estoque"),
)

class PRODUTO(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    photo_prod = models.ImageField(upload_to = "img/%y")
    preco = models.DecimalField(max_digits = 10, decimal_places=2)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(
        max_length = 50,
        choices = Status,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

