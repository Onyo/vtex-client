# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import responses
from unittest import TestCase

from vtex_client import faults
from vtex_client import TransactionClient

from . import mockup


class CreateTransactionTestCase(TestCase):

    def setUp(self):
        self.client = TransactionClient(api_store="teststore",
                                        api_key="testkey",
                                        api_token="testtoken")
        self.url = "https://teststore.vtexpayments.com.br/api/pvt/transactions"
        self.data = {"value": 100,
                     "referenceId": "REF001",
                     "channel": "mychannel",
                     "urn": ""}

    @responses.activate
    def test_ok(self):
        response_body, response_data = mockup.get_success()
        responses.add(responses.POST,
                      self.url,
                      body=response_body,
                      status=200,
                      content_type='text/json')

        result = self.client.create(self.data)
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
            self.client.create(self.data)

        self.assertEqual(context.exception.message, "Acesso não autorizado")
        self.assertEqual(context.exception.code, "1")

    @responses.activate
    def test_invalid_data_without_value(self):
        response_body = mockup.get_invalid_data_error()
        responses.add(responses.POST,
                      self.url,
                      body=response_body,
                      status=400,
                      content_type='text/json')

        del self.data['value']

        with self.assertRaises(faults.InvalidDataError) as context:
            self.client.create(self.data)

        self.assertIn("make sure the transaction value is greater than zero",
                      context.exception.message)
        self.assertEqual(context.exception.code, "1402")

    @responses.activate
    def test_invalid_data_without_reference_id(self):
        response_body = mockup.get_invalid_data_error()
        responses.add(responses.POST,
                      self.url,
                      body=response_body,
                      status=400,
                      content_type='text/json')

        del self.data['referenceId']

        with self.assertRaises(faults.InvalidDataError) as context:
            self.client.create(self.data)

        self.assertIn("paramaters must be different from null or whitespace",
                      context.exception.message)
        self.assertEqual(context.exception.code, "1402")
