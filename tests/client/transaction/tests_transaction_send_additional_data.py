# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import responses
from unittest import TestCase

from vtex_client import faults
from vtex_client.transaction import TransactionClient

from . import mockup


class SendAdditionalDataTestCase(TestCase):

    def setUp(self):
        self.id = "BB55ED929FF749E6BE5A835E4C811B77"
        self.client = TransactionClient(api_store="teststore",
                                        api_key="testkey",
                                        api_token="testtoken")
        self.url = "https://teststore.vtexpayments.com.br/api/pvt/"\
                   "transactions/{}/additional-data".format(self.id)
        self.data = [
            {
                "name": "cart",
                "value": '{"items":[],"freight":0,"tax":0}'
            },
            {
                "name": "clientProfileData",
                "value": """{
                    "id":"1234",
                    "email":"teste@teste.com",
                    "firstName":"Joao",
                    "lastName":"null",
                    "document":"null",
                    "phone":"null",
                    "corporateName":null,
                    "tradeName":null,
                    "corporateDocument":null,
                    "stateInscription":null,
                    "postalCode":"22011-050",
                    "gender":null,
                    "birthDate":null,
                    "corporatePhone":null,
                    "isCorporate":false
                    "address":{
                        "receiverName":"null",
                        "postalCode":"null",
                        "city":"null",
                        "state":"RJ",
                        "country":"BRA",
                        "street":"null",
                        "number":"null",
                        "neighborhood":"null",
                        "complement":"null",
                        "reference":null
                    },
                }"""
            },
            {
                "name": "shippingData",
                "value": """{
                    "receiverName":"null",
                    "postalCode":"null",
                    "city":"null",
                    "state":"RJ",
                    "country":"null",
                    "street":"null",
                    "number":"null",
                    "neighborhood":"null",
                    "complement":"null",
                    "reference":null
                }"""
            }
        ]

    @responses.activate
    def test_ok(self):
        responses.add(responses.POST,
                      self.url,
                      body="",
                      status=200,
                      content_type='text/json')

        result = self.client.send_additional_data(self.id, self.data)
        self.assertEqual(result, {})
