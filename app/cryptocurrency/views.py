from drf_spectacular.utils import extend_schema_view, extend_schema
from eth_account import Account
from rest_framework import status, viewsets
from rest_framework.response import Response

from cryptocurrency import serializers
from cryptocurrency.models import Wallet


@extend_schema_view(
    list=extend_schema(
        summary="Получить список всех кошельков.",
        description="Получить список всех кошельков.",
        tags=["Кошельки"],
    ),
    create=extend_schema(
        summary="Создать кошелек.",
        description="Создать кошелек.",
        tags=["Кошельки"],
    ),
)
class WalletViewSet(viewsets.GenericViewSet):
    queryset = Wallet.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.CreateWalletSerializer
        elif self.action == "list":
            return serializers.ListWalletSerializer

    def create(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        account = Account.create()

        data = {
            "currency": serializer.data["currency"],
            "public_key": account.address,
            "private_key": account.key.hex(),
        }

        instance = Wallet.objects.create(**data)
        serializer = serializers.RetrieveWalletSerializer(instance=instance)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance=self.queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

