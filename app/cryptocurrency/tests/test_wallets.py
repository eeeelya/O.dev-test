import pytest
from rest_framework import status
from unittest.mock import MagicMock


@pytest.mark.django_db
@pytest.mark.parametrize(
    "payload, expected_code", [
        ({}, status.HTTP_400_BAD_REQUEST),
        ({"currency": "BTC"}, status.HTTP_400_BAD_REQUEST),
        ({"currency": "ETH"}, status.HTTP_201_CREATED),
    ]
)
def test_create_wallet(api_client, mocker, payload, expected_code):
    account_mock = MagicMock()
    account_mock.address = "test_address"
    account_mock.key.hex.return_value = "test_key"

    mocker.patch("eth_account.Account.create", return_value=account_mock)

    response = api_client.post("/api/v1/wallets/", data=payload)

    assert response.status_code == expected_code


@pytest.mark.django_db
def test_get_all_wallets(api_client, mocker, wallets):
    mocker.patch("cryptocurrency.serializers.ListWalletSerializer.get_balance", return_value="")

    response = api_client.get("/api/v1/wallets/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10
