from rest_framework import serializers
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

from reader.models import Reader


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"

class ReaderSerializerView(serializers.ModelSerializer):
    tipo = TransactionSerializer()

    class Meta:
        model = Reader
        fields = "__all__"
