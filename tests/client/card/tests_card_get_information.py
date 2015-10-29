# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import responses
from unittest import TestCase

from vtex_client import faults
from vtex_client.card import CardClient


class CreateTransactionTestCase(TestCase):

    def setUp(self):
        self.client = CardClient()
        self.url = "https://api.vtexpayments.com.br/api/pvt/bins"

    @responses.activate
    def test_ok(self):
        response = [
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
        response_body = json.dumps(response)
        numbers = '123456'
        responses.add(responses.GET,
                      self.url,
                      body=response_body,
                      status=200,
                      content_type='text/json')

        result = self.client.get_information(numbers)
        self.assertEqual(result, response)

    @responses.activate
    def test_card_not_found(self):
        numbers = '000000'
        responses.add(responses.GET,
                      self.url,
                      body="[]",
                      status=200,
                      content_type='text/json')

        result = self.client.get_information(numbers)
        self.assertEqual(result, [])

    @responses.activate
    def test_invalid_parameter(self):
        """ Test sending parameter over six numbers"""
        response = {
            "Message": "An error has occurred."
        }
        response_body = json.dumps(response)
        numbers = '1234567890'
        responses.add(responses.GET,
                      self.url,
                      body=response_body,
                      status=500,
                      content_type='text/json')

        with self.assertRaises(faults.GetewayError):
            self.client.get_information(numbers)
