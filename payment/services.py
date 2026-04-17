import json
import requests
from django.conf import settings


#try to make a post request to paystack endpoint
def checkout(payload ):
    headers = {
        "Authorization":f"Bearer{"SECRET_KEY"}", # leting paystack know who his passing the request
        "Content-Type": "application/json"    
    }

    response = requests.post(
        "https://api.paystack.co/tranaction/initialize",
        headers=headers,
        data=json.dump(payload)
    )

    response_data = response.json()
    {
        "email": "",
        "amount": 0,
        "currenc y":"NGN",
        "channel":["card","bank_transfer", "bank","ussd", "qr","mobile_money"],
        "reference":"purchase_001_xyz",
        "callback_url":"product_id"
        "metadata":{
            product_id:product_id,
            "user_id":1
        }
        "label":"checkout for product 3"

    
    }