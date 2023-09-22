from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from web3 import Web3

from cryptocurrency.models import Wallet
from odev.settings import INFRUA_ID


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
    balance = serializers.SerializerMethodField()

    def get_balance(self, obj):
        w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFRUA_ID}"))

        if not w3.is_connected():
            raise ValidationError("Can't connect to infrua.io")

        balance_wei = w3.eth.get_balance(obj.public_key)

        return w3.from_wei(balance_wei, 'ether')

    class Meta:
        model = Wallet
        fields = ["id", "currency", "public_key", "balance"]
