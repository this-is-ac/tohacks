from trycourier import Courier


def send_alert():
    client = Courier(auth_token="pk_prod_ZQ6A3QEYEZ4SBTJS5VRX7MFQ7XE9")

    resp = client.send(
        event="courier-quickstart",
        recipient="Google_115944001700649782549",
        data={
            "favoriteAdjective": "awesomeness"
        }
    )

    print(resp['messageId'])