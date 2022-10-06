from uuid import uuid4

from django.db import models
from transactions.models import Transation

# Create your models here.


class Reader(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    tipo = models.ForeignKey(
        Transation,
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    data = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    cpf = models.CharField(max_length=11)
    cartão = models.CharField(max_length=12)
    hora = models.TimeField()
    dono_da_loja = models.CharField(max_length=127)
    nome_da_loja = models.CharField(max_length=127)
