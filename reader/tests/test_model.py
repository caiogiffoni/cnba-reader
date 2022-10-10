# actors/tests/test_models.py
from csv import reader

from django.test import TestCase
from reader.models import Reader
from transactions.models import Transaction


class ReaderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.transaction = Transaction.objects.create(
            tipo=3,
            descrição="Financiamento",
            natureza="Saída",
            sinal=-1,
        )
        cls.text = (
            "3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR"
            " DO JOÃO"
        )

        cls.data = {
            "data": f"{cls.text[1:5]}-{cls.text[5:7]}-{cls.text[7:9]}",
            "valor": float(cls.text[9:19]) / 100,
            "cpf": cls.text[19:30],
            "cartão": cls.text[30:42],
            "hora": f"{cls.text[42:44]}:{cls.text[44:46]}:{cls.text[46:48]}",
            "dono_da_loja": cls.text[48:62].strip(),
            "nome_da_loja": cls.text[62:81].strip(),
            "tipo": cls.transaction,
        }

        cls.reader = Reader.objects.create(**cls.data)

    def test_reader_max_length(self):
        max_length_owner = self.reader._meta.get_field(
            "dono_da_loja"
        ).max_length
        max_length_name = self.reader._meta.get_field(
            "nome_da_loja"
        ).max_length
        max_length_cpf = self.reader._meta.get_field("cpf").max_length
        max_length_card = self.reader._meta.get_field("cartão").max_length
        self.assertEquals(max_length_owner, 127)
        self.assertEquals(max_length_name, 127)
        self.assertEquals(max_length_card, 12)
        self.assertEquals(max_length_cpf, 11)

    def test_reader_has_information_fields(self):
        self.assertEqual(self.reader.tipo, self.transaction)
        self.assertEqual(self.reader.data, self.data["data"])
        self.assertEqual(self.reader.valor, self.data["valor"])
        self.assertEqual(self.reader.cpf, self.data["cpf"])
        self.assertEqual(self.reader.cartão, self.data["cartão"])
        self.assertEqual(self.reader.hora, self.data["hora"])
        self.assertEqual(self.reader.dono_da_loja, self.data["dono_da_loja"])
        self.assertEqual(self.reader.nome_da_loja, self.data["nome_da_loja"])

    def test_reader_balance(self):
        self.assertEqual(self.reader.tipo, self.transaction)
        transaction_cre = Transaction.objects.create(
            tipo=2,
            descrição="Boleto",
            natureza="Saída",
            sinal=-1,
        )
        transaction_alu = Transaction.objects.create(
            tipo=1,
            descrição="Débito",
            natureza="Entrada",
            sinal=1,
        )

        text_t2 = (
            "2201903010000011200096206760173648****0099234234JOÃO MACEDO   BAR"
            " DO JOÃO   "
        )

        data_t2 = {
            "data": f"{text_t2[1:5]}-{text_t2[5:7]}-{text_t2[7:9]}",
            "valor": float(text_t2[9:19]) / 100,
            "cpf": text_t2[19:30],
            "cartão": text_t2[30:42],
            "hora": f"{text_t2[42:44]}:{text_t2[44:46]}:{text_t2[46:48]}",
            "dono_da_loja": text_t2[48:62].strip(),
            "nome_da_loja": text_t2[62:81].strip(),
            "tipo": transaction_cre,
        }

        reader_t2 = Reader.objects.create(**data_t2)

        text_t3 = (
            "1201903010000015200096206760171234****7890233000JOÃO MACEDO   BAR"
            " DO JOÃO   "
        )

        data_t3 = {
            "data": f"{text_t3[1:5]}-{text_t3[5:7]}-{text_t3[7:9]}",
            "valor": float(text_t3[9:19]) / 100,
            "cpf": text_t3[19:30],
            "cartão": text_t3[30:42],
            "hora": f"{text_t3[42:44]}:{text_t3[44:46]}:{text_t3[46:48]}",
            "dono_da_loja": text_t3[48:62].strip(),
            "nome_da_loja": text_t3[62:81].strip(),
            "tipo": transaction_alu,
        }

        reader_t3 = Reader.objects.create(**data_t3)

        balance = (
            (self.reader.tipo.sinal * self.reader.valor)
            + (reader_t2.tipo.sinal * reader_t2.valor)
            + (reader_t3.tipo.sinal * reader_t3.valor)
        )
        self.assertEquals(balance, -102)
