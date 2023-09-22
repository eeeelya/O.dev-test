from django.db import models

from cryptocurrency.utils import generate_uuid


class CurrencyChoices(models.TextChoices):
    """According to the task, we can only use ETH, but this is a good option for future development"""
    ETHEREUM = "ETH", "Ethereum"


class Wallet(models.Model):
    id = models.CharField(default=generate_uuid, primary_key=True, editable=False, max_length=40)
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices, default=CurrencyChoices.ETHEREUM.value)
    public_key = models.CharField(default="")
    private_key = models.CharField(default="")

