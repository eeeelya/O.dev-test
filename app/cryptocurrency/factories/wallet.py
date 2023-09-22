import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from cryptocurrency.models import Wallet, CurrencyChoices


class WalletFactory(DjangoModelFactory):
    public_key = fuzzy.FuzzyText(length=40)
    private_key = fuzzy.FuzzyText(length=40)
    currency = factory.fuzzy.FuzzyChoice(CurrencyChoices)

    class Meta:
        model = Wallet
