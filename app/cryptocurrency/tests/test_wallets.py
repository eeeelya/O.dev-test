from unittest.mock import Mock

import eth_account
import pytest
from rest_framework import status


@pytest.mark.django_db
@pytest.mark.parametrize(
    "payload, expected_code", [
        ({}, status.HTTP_400_BAD_REQUEST),
        ({"currency": "BTC"}, status.HTTP_400_BAD_REQUEST),
        ({"currency": "ETH"}, status.HTTP_200_OK),
    ]
)
def test_create_wallet(api_client, mocker, payload, expected_code):
    mocker.patch("eth_account.Account.create")

    response = api_client.post("/api/v1/wallets/", data=payload)

    assert response.status_code == expected_code


@pytest.mark.django_db
def test_get_all_wallets(api_client, mocker, wallets):
    mocker.patch("web3.Web3.HTTPProvider")
    mocker.patch("web3.Web3")

    response = api_client.get("/api/v1/wallets/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10
