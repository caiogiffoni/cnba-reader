from rest_framework import serializers

from reader.models import Reader


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"
