import modulefinder
from uuid import uuid4

from django.db import models

# Create your models here.


class Transation(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    tipo = models.SmallIntegerField()
    descrição = models.CharField(max_length=127)
    natureza = models.CharField(max_length=127)
    sinal = models.IntegerField()
