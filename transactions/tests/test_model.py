# actors/tests/test_models.py

from sqlite3 import IntegrityError

from django.test import TestCase
from transactions.models import Transaction


class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tipo = 1
        cls.descrição = "Multa"
        cls.natureza = "Entrada"
        cls.sinal = -1

        cls.transaction = Transaction.objects.create(
            tipo=cls.tipo,
            descrição=cls.descrição,
            natureza=cls.natureza,
            sinal=cls.sinal,
        )

    def test_name_max_length(self):
        max_length_desc = self.transaction._meta.get_field(
            "descrição"
        ).max_length
        max_length_nat = self.transaction._meta.get_field(
            "natureza"
        ).max_length
        self.assertEquals(max_length_desc, 127)
        self.assertEquals(max_length_nat, 127)

    def test_transaction_has_information_fields(self):
        self.assertEqual(self.transaction.tipo, self.tipo)
        self.assertEqual(self.transaction.descrição, self.descrição)
        self.assertEqual(self.transaction.natureza, self.natureza)
        self.assertEqual(self.transaction.sinal, self.sinal)

    def test_transaction_has_unique_tipo(self):
        transaction_1 = {
            "tipo": 1,
            "descrição": "Multa",
            "natureza": "Entrada",
            "sinal": -1,
        }
        try:
            Transaction.objects.create(**transaction_1)
        except:
            return True
        return False
