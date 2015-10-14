# Usage

- [Create transaction](#create)
- [Get transaction](#get)
- [Authorize transaction](#authorize)
- [Capture transaction](#capture)
- [Cancel transaction](#cancel)
- [Get Payment info](#get-payment)
- [Send Payment](#send-payment)



## <a name="create"></a>Create transaction
```python
from vtex_client import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
data = {"value": 100,
        "referenceId": "REF001",
        "channel": "mychannel",
        "urn": ""}

result = self.client.create(self.data)
```


## <a name="get"></a>Get transaction
```python
from vtex_client import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")

transaction = "$TRANSACTION_ID"
result = self.client.get(transaction)
```


## <a name="authorize"></a>Authorize transaction
```python
from vtex_client import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
transaction = "$TRANSACTION_ID"
data = {'prepareForRecurrency': False,
        'softDescriptor': 'myConmpany',
        'split': [],
        'transactionId': transaction}

result = self.client.authorize(transaction, data)
```

## <a name="capture"></a>Capture transaction
```python
from vtex_client import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
transaction = "$TRANSACTION_ID"
result = self.client.capture(transaction, value=100)
```

## <a name="cancel"></a>Cancel transaction
```python
from vtex_client import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
transaction = "$TRANSACTION_ID"
result = self.client.cancel(transaction, value=100)
```

## <a name="get-payment"></a>Get Payment Information
```python
from vtex_client import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")

result = self.client.get_payment("$TRANSACTION_ID")
```


## <a name="send-payment"></a>Send Payment Information
```python
from vtex_client import TransactionClient

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
result = self.client.get_payment(data)
```
