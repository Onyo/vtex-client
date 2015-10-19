# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import responses
from unittest import TestCase

from vtex_client import faults
from vtex_client.transaction import TransactionClient

from . import mockup


class GetTransactionPaymentTestCase(TestCase):

    def setUp(self):
        self.id = "BB55ED929FF749E6BE5A835E4C811B77"
        self.client = TransactionClient(api_store="teststore",
                                        api_key="testkey",
                                        api_token="testtoken")
        self.url = "https://teststore.vtexpayments.com.br/api/pvt/"\
                   "transactions/{}/payments".format(self.id)

    @responses.activate
    def test_ok(self):
        response_body, response_data = mockup.get_payment_success()
        responses.add(responses.GET,
                      self.url,
                      body=response_body,
                      status=200,
                      content_type='text/json')

        result = self.client.get_payment(self.id)
        self.assertEqual(result, response_data)

    @responses.activate
    def test_authorization_error(self):
        response_body = mockup.get_authorization_error()
        responses.add(responses.GET,
                      self.url,
                      body=response_body,
                      status=401,
                      content_type='text/json')

        with self.assertRaises(faults.AuthorizationError) as context:
            self.client.get_payment(self.id)

        self.assertEqual(context.exception.message, "Acesso não autorizado")
        self.assertEqual(context.exception.code, "1")

    @responses.activate
    def test_not_found(self):
        response_body = mockup.get_authorization_error()
        responses.add(responses.GET,
                      self.url,
                      body="null",
                      status=200,
                      content_type='text/json')

        result = self.client.get_payment(self.id)

        self.assertEqual(result, None)
