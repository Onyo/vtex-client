# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import responses
from unittest import TestCase

from vtex_client import faults
from vtex_client.transaction import TransactionClient

from . import mockup


class AuthorizeTransactionTestCase(TestCase):

    def setUp(self):
        self.id = "BB55ED929FF749E6BE5A835E4C811B77"
        self.client = TransactionClient(api_store="teststore",
                                        api_key="testkey",
                                        api_token="testtoken")
        self.url = "https://teststore.vtexpayments.com.br/api/pvt/"\
                   "transactions/{}/authorization-request".format(self.id)
        self.data = {
            "transactionId": self.id,
            "softDescriptor": "sandboxintegracao",
            "prepareForRecurrency": False,
            "split": []
        }

    @responses.activate
    def test_ok(self):
        response_body, response_data = mockup.get_authorize_success()
        responses.add(responses.POST,
                      self.url,
                      body=response_body,
                      status=200,
                      content_type='text/json')

        result = self.client.authorize(self.id, self.data)
        self.assertEqual(result, response_data)

    @responses.activate
    def test_authorization_error(self):
        response_body = mockup.get_authorization_error()
        responses.add(responses.POST,
                      self.url,
                      body=response_body,
                      status=401,
                      content_type='text/json')

        with self.assertRaises(faults.AuthorizationError) as context:
            self.client.authorize(self.id, self.data)

        self.assertEqual(context.exception.message, "Acesso não autorizado")
        self.assertEqual(context.exception.code, "1")

    @responses.activate
    def test_without_payment(self):
        response_body = mockup.get_without_payment_error()
        responses.add(responses.POST,
                      self.url,
                      body=response_body,
                      status=400,
                      content_type='text/json')

        with self.assertRaises(faults.InvalidDataError) as context:
            self.client.authorize(self.id, self.data)

        self.assertEqual("The transaction does not have any payments.",
                         context.exception.message)
        self.assertEqual(context.exception.code, "1419")
