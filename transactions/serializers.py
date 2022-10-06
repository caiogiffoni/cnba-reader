from rest_framework import serializers

from transactions.models import Transation


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transation
        fields = "__all__"
