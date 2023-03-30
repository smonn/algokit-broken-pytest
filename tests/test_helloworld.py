from beaker.client import ApplicationClient
from beaker.sandbox import get_accounts, get_algod_client

from smart_contracts.helloworld import app

accounts = get_accounts()
sender = accounts[0]
algod = get_algod_client()

app_client = ApplicationClient(app=app, client=algod, sender=sender.address, signer=sender.signer)


def test_create_helloworld() -> None:
    app_client.create()
