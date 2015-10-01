# Usage

## Create transaction
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

## Authorize transaction
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

## Get Payment Information
```python
from vtex_client import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")

result = self.client.get_payment("$TRANSACTION_ID")
```
