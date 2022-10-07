from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

        extra_kwargs = {
            "tipo": {
                "validators": [
                    UniqueValidator(
                        queryset=Transaction.objects.all(),
                        message="This tipo number already exists",
                    )
                ]
            }
        }

    # def validate_sinal(self, sinal):   VALIDATION TO BE IMPLEMENTED AFTER
    #     if sinal == 0:
    #         raise serializers.ValidationError(
    #             "The sinal field must be -1 or +1 digits"
    #         )
    #     return sinal
