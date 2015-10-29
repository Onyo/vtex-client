# Usage

- [Create transaction](#create)
- [Get transaction](#get)
- [Authorize transaction](#authorize)
- [Capture transaction](#capture)
- [Cancel transaction](#cancel)
- [Get Payment info](#get-payment)
- [Send Payment](#send-payment)
- [Get public information about credit card](#card-getinformation)




## <a name="create"></a>Create transaction
```python
from vtex_client.transaction import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
data = {"value": 100,
        "referenceId": "REF001",
        "channel": "mychannel",
        "urn": ""}

result = client.create(data)
```


## <a name="get"></a>Get transaction
```python
from vtex_client.transaction import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")

transaction = "$TRANSACTION_ID"
result = client.get(transaction)
```


## <a name="authorize"></a>Authorize transaction
```python
from vtex_client.transaction import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
transaction = "$TRANSACTION_ID"
data = {'prepareForRecurrency': False,
        'softDescriptor': 'myCompany',
        'split': [],
        'transactionId': transaction}

result = client.authorize(transaction, data)
```

## <a name="capture"></a>Capture transaction
```python
from vtex_client.transaction import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
transaction = "$TRANSACTION_ID"
result = client.capture(transaction, value=100)
```

## <a name="cancel"></a>Cancel transaction
```python
from vtex_client.transaction import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
transaction = "$TRANSACTION_ID"
result = client.cancel(transaction, value=100)
```

## <a name="get-payment"></a>Get Payment Information
```python
from vtex_client.transaction import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")

result = client.get_payment("$TRANSACTION_ID")
```


## <a name="send-payment"></a>Send Payment Information
```python
from vtex_client.transaction import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
data = [
    {
        "paymentSystem": 2,
        "paymentSystemName": "Visa",
        "groupName": "creditCard",
        "currencyCode": "BRL",
        "installments": 1,
        "value": 100,
        "installmentsInterestRate": 0,
        "installmentsValue": 100,
        "referenceValue": 100,
        "fields": {
            "accountId": "$ACCOUNT_ID",
            "validationCode": "123"
        },
        "transaction": {
            "id": "$TRANSACTION_ID",
            "merchantName": "test"
        }
    }
]
result = client.get_payment(data)
```


## <a name="card-getinformation"></a>Get public information about credit card
```python
from vtex_client.card import CardClient

client = CardClient()
result = client.get_information("$FIRST_6_NUMBERS_OF_CARD")
print result
[
    {
        "id": "f0696ef3-1dea-5ae0-9db2-8e581fc229c6",
        "code": 546785,
        "cardBrand": "visa",
        "cardCoBrand": None,
        "cardType": None,
        "country": {
            "name": "Brazil",
            "isoCode": "BR",
            "isoCodeThreeDigits": "BRA"
        },
        "bank": {
            "issuer": "BANCO DO BRASIL S.A.",
            "website": None,
            "phone": None,
            "address": None
        },
        "cvvSize": 3,
        "expirable": True,
        "validationAlgorithm": "LUHN",
        "additionalInfo": None,
        "cardLevel": "CLASSIC"
    }
]
```
