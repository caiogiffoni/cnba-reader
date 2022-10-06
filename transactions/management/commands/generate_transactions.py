# create_multiple_users.py

from django.core.management.base import BaseCommand
from transactions.models import Transation

table = [
    {
        "tipo": 1,
        "descrição": "Débito",
        "natureza": "Entrada",
        "sinal": 1,
    },
    {
        "tipo": 2,
        "descrição": "Boleto",
        "natureza": "Saída",
        "sinal": -1,
    },
    {
        "tipo": 3,
        "descrição": "Financiamento",
        "natureza": "Saída",
        "sinal": -1,
    },
    {
        "tipo": 4,
        "descrição": "Crédito",
        "natureza": "Entrada",
        "sinal": 1,
    },
    {
        "tipo": 5,
        "descrição": "Recebimento Empréstimo",
        "natureza": "Entrada",
        "sinal": 1,
    },
    {
        "tipo": 6,
        "descrição": "Vendas",
        "natureza": "Entrada",
        "sinal": 1,
    },
    {
        "tipo": 7,
        "descrição": "Recebimento TED",
        "natureza": "Entrada",
        "sinal": 1,
    },
    {
        "tipo": 8,
        "descrição": "Recebimento DOC",
        "natureza": "Entrada",
        "sinal": 1,
    },
    {
        "tipo": 9,
        "descrição": "Aluguel",
        "natureza": "Saída",
        "sinal": -1,
    },
]


class Command(BaseCommand):
    help = "Create transactions table"

    def handle(self, *args, **kwargs):
        Transation.objects.bulk_create(
            [Transation(**el) for el in table]
        )  ## BULK CREATTE FOR PERFOMANCE
