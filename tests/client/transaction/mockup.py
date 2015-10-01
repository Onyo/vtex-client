# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json


transaction_data = {
    "id": "",
    "transactionId": "",
    "referenceKey": "",
    "interactions": {
        "href": "/api/pvt/transactions/{}/interactions"
    },
    "settlements": {
        "href": "/api/pvt/transactions/{}/settlements"
    },
    "payments": {
        "href": "/api/pvt/transactions/{}/payments"
    },
    "refunds": {
        "href": "/api/pvt/transactions/{}/refunds"
    },
    "cancellations": {
        "href": "/api/pvt/transactions/{}/cancellations"
    },
    "timeoutStatus": 0,
    "totalRefunds": 0,
    "status": "Started",
    "value": 100,
    "receiverUri": "https://teststore.vtexpayments.com.br/split/{}/payments",
    "startDate": "2015-01-01T00:00:00",
    "authorizationToken": None,
    "authorizationDate": None,
    "commitmentToken": None,
    "commitmentDate": None,
    "refundingToken": None,
    "refundingDate": None,
    "cancelationToken": None,
    "cancelationDate": None,
    "fields": [
        {
            "name": "owner",
            "value": "testkey"
        },
        {
            "name": "channel",
            "value": "teststore"
        },
        {
            "name": "salesChannel",
            "value": None
        }
    ],
    "ipAddress": None,
    "owner": "testkey",
    "userAgent": None,
    "acceptHeader": None,
    "antifraudTid": None,
    "antifraudAffiliationId": None,
    "channel": "onyo",
    "salesChannel": None,
    "urn": None,
    "softDescriptor": None,
    "markedForRecurrence": False,
    "buyer": None
}


error_data = {
    "error": {
        "code": "",
        "message": "",
        "exception": {}
    }
}


def get_success():
    transaction_id = 'd9729feb74992cc3482b350163a1a010'

    data = dict(transaction_data)
    data.update({
        "id": transaction_id,
        "transactionId": transaction_id,
        "receiverUri": data['receiverUri'].format(transaction_id),
        "interactions": {
            "href": data['interactions']['href'].format(transaction_id)
        },
        "settlements": {
            "href": data['settlements']['href'].format(transaction_id)
        },
        "payments": {
            "href": data['payments']['href'].format(transaction_id)
        },
        "refunds": {
            "href": data['refunds']['href'].format(transaction_id)
        },
        "cancellations": {
            "href": data['cancellations']['href'].format(transaction_id)
        },
    })
    return json.dumps(data), data


def get_authorization_error():
    data = dict(error_data)
    data['error']['message'] = "Acesso não autorizado"
    data['error']['code'] = "1"
    return json.dumps(data)


def get_invalid_data_error():
    data = dict(error_data)
    data['error']['code'] = "1402"
    data['error']['message'] = "The transaction creation request and its "\
        "paramaters must be different from null or whitespace. Also, make "\
        "sure the transaction value is greater than zero."
    return json.dumps(data)
