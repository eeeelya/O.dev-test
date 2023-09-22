from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cryptocurrency.models import Wallet


class CreateWalletSerializer(serializers.ModelSerializer):
    def validate_currency(self, value):
        if value != "ETH":
            return ValidationError("Only ETH is supported.")

        return value

    class Meta:
        model = Wallet
        fields = ["currency"]
        extra_kwargs = {"currency": {"required": True}}


class RetrieveWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "currency", "public_key"]


class ListWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "currency", "public_key"]
