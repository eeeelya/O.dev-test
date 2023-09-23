import pytest
from rest_framework.test import APIClient

from cryptocurrency.factories.wallet import WalletFactory


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def wallets():
    WalletFactory.create_batch(size=10)
