# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import responses
from unittest import TestCase

from vtex_client import faults
from vtex_client import TransactionClient

from . import mockup


class SendTransactionPaymentTestCase(TestCase):

    def setUp(self):
        self.id = "BB55ED929FF749E6BE5A835E4C811B77"
        self.client = TransactionClient(api_store="teststore",
                                        api_key="testkey",
                                        api_token="testtoken")
        self.url = "https://teststore.vtexpayments.com.br/api/pvt/"\
                   "transactions/{}/payments".format(self.id)
        self.data = [
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
                    "accountId": "AJA4CF6058ED44BD9A3637F43C0BAA5Y",
                    "validationCode": "123"
                },
                "transaction": {
                    "id": self.id,
                    "merchantName": "test"
                }
            }
        ]

    @responses.activate
    def test_ok(self):
        responses.add(responses.POST,
                      self.url,
                      body="",
                      status=200,
                      content_type='text/json')

        result = self.client.send_payment(self.id, self.data)
        self.assertEqual(result, {})

    @responses.activate
    def test_invalid_data(self):
        body, response_data = mockup.send_payment_invalid_data_error(
            self.id)
        responses.add(responses.POST,
                      self.url,
                      body=body,
                      status=400,
                      content_type='text/json')

        with self.assertRaises(faults.InvalidDataError) as context:
            self.client.send_payment(self.id, self.data)

        self.assertIn("Error when receiving payments for transaction",
                      context.exception.message)
        self.assertEqual(context.exception.code, "1414")
