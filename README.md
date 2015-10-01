# vtex-client

The VTEX Client is a library to connect your Python apps to VTEX Payment Gateway (http://www.vtex.com/payment/).

## Overview

- VTEX uses JSON in requests and responses data
- The library does not validate the request data before sending it to keep compatibility with future updates in the VTEX API

All information about data specifications and flows can be found at the following links:
- http://lab.vtex.com/
- http://vtex.github.io/docs/integracao/marketplace/canal-de-vendas-nao-vtex-com-pgto/index.html

## Installation
```
pip install git+https://github.com/Onyo/vtex-client.git
```

## Requirements
Python (2.6 > or 3.x)

## Usage
Exemple of creating transaction:
```python
from vtex_client import TransactionClient

client = TransactionClient(api_store="$MY_STORE",
                           api_key="$MY_KEY",
                           api_token="$MY_TOKEN")
data = {"value": 100,
        "referenceId": "REF001",
        "channel": "mychannel",
        "urn": ""}

# Result is a dictionary of all transaction data
result = self.client.create(self.data)
```

[See all usage documentation](USAGE.md)

## Running tests
```
nosetests
```


## Reporting issues and contributing

If you find any bugs or have any suggestion for improvement, please
file an issue at https://github.com/Onyo/vtex-client/issues. Do not
contact the authors directly by mail, as this increases the chance
of your report being lost.

If you created a patch, please submit a [Pull
Request](https://github.com/Onyo/vtex-client/pulls).


## License

This library is released under the [GNU General Public License version
3](http://www.gnu.org/licenses/gpl-3.0.html).
