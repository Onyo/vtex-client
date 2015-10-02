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


def create_transaction_success():
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


def create_transaction_invalid_data_error():
    data = dict(error_data)
    data['error']['code'] = "1402"
    data['error']['message'] = "The transaction creation request and its "\
        "paramaters must be different from null or whitespace. Also, make "\
        "sure the transaction value is greater than zero."
    return json.dumps(data)


def send_payment_invalid_data_error(transaction):
    data = dict(error_data)
    data['error']['code'] = "1414"
    data['error']['message'] = "Error when receiving payments for transaction"\
                               " = {}. Please, "\
                               "see the logs for details.".format(transaction)
    return json.dumps(data), data


def get_without_payment_error():
    data = dict(error_data)
    data['error']['code'] = "1419"
    data['error']['message'] = "The transaction does not have any payments."
    return json.dumps(data)


def get_authorize_success():
    data = {
        "token": "124053A3D81E4416A63CDD5882EF83D2",
        "status": 8,
        "statusDetail": "Approved",
        "processingDate": "2015-09-01T19:07:09.2113805Z",
        "refundedValue": 0,
        "refundedToken": None,
        "message": None,
        "connectorRefundedValue": 0,
        "cancelledValue": 0
    }
    return json.dumps(data), data


def get_payment_success():
    data = [
        {
            "id": "2C1927BEA6854",
            "paymentSystem": 2,
            "paymentSystemName": "Visa",
            "group": "creditCard",
            "isCustom": False,
            "allowInstallments": True,
            "allowIssuer": True,
            "allowNotification": False,
            "isAvailable": True,
            "description": None,
            "self": {
                "href": "/api/pvt/transactions/2C1927BEA6854/payments/BAEE1047"
            },
            "tid": None,
            "returnCode": "-1004",
            "returnMessage": "Cardholder is empty",
            "status": "Cancelled",
            "connector": "Cielo",
            "ConnectorResponses": {
                "Tid": None,
                "ReturnCode": "-1004",
                "Message": "Cardholder is empty"
            },
            "connectorResponse": {
                "Tid": None,
                "ReturnCode": "-1004",
                "Message": "Cardholder is empty"
            },
            "ShowConnectorResponses": True,
            "value": 100,
            "installmentsInterestRate": 0,
            "installmentsValue": 100,
            "referenceValue": 100,
            "installments": 1,
            "currencyCode": "BRL",
            "provider": None,
            "fields": [
                {
                    "name": "affiliationId",
                    "value": "215b2709-"
                },
                {
                    "name": "callbackUrl",
                    "value": ""
                },
                {
                    "name": "baseUrl",
                    "value": "https://test.vtexpayments.com.br:443"
                },
                {
                    "name": "currencyCode",
                    "value": "BRL"
                },
                {
                    "name": "cardHolder",
                    "value": ""
                },
                {
                    "name": "firstDigits",
                    "value": "444433"
                },
                {
                    "name": "lastDigits",
                    "value": "1111"
                },
                {
                    "name": "expiryMonth",
                    "value": "10"
                },
                {
                    "name": "expiryYear",
                    "value": "2020"
                },
                {
                    "name": "accountId",
                    "value": "4324RG434356WWHG24"
                },
                {
                    "name": "connector",
                    "value": "Vtex.PaymentGateway.Connectors.CieloConnector"
                },
                {
                    "name": "returnCode",
                    "value": "-1004"
                },
                {
                    "name": "returnMessage",
                    "value": "Cardholder is empty"
                }
            ],
            "sheets": None
        }
    ]
    return json.dumps(data), data


def cancel_transaction_success():
    data = {
        'cancelledValue': 0,
        'connectorRefundedValue': 0,
        'message': None,
        'processingDate': '2015-10-02T19:07:15.9803356Z',
        'refundedToken': None,
        'refundedValue': 0,
        'status': 10,
        'statusDetail': 'Cancelled',
        'token': '1B6E27DCE2B9453C8',
    }
    return json.dumps(data), data


def cancel_transaction_invalid_data_error():
    data = dict(error_data)
    data['error']['code'] = "1402"
    data['error']['message'] = "The transaction value passed (0) is different"\
        "from persisted transaction value (1.00). A possible cause is that "\
        "the transaction for cancellation is another one (Id = ABC)."
    return json.dumps(data)
