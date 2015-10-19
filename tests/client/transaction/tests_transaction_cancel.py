# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import responses
from unittest import TestCase

from vtex_client import faults
from vtex_client.transaction import TransactionClient

from . import mockup


class CancelTransactionTestCase(TestCase):

    def setUp(self):
        self.id = "BB55ED929FF749E6BE5A835E4C811B77"
        self.client = TransactionClient(api_store="teststore",
                                        api_key="testkey",
                                        api_token="testtoken")
        self.url = "https://teststore.vtexpayments.com.br/api/pvt/"\
                   "transactions/{}/cancellation-request".format(self.id)

    @responses.activate
    def test_ok(self):
        body, response_data = mockup.cancel_transaction_success()
        responses.add(responses.POST,
                      self.url,
                      body=body,
                      status=200,
                      content_type='text/json')

        result = self.client.cancel(self.id, 100)
        self.assertEqual(result, response_data)

    @responses.activate
    def test_invalid_data(self):
        body = mockup.cancel_transaction_invalid_data_error()
        responses.add(responses.POST,
                      self.url,
                      body=body,
                      status=400,
                      content_type='text/json')

        with self.assertRaises(faults.InvalidDataError) as context:
            self.client.cancel(self.id, 0)

        self.assertIn("The transaction value passed (0) is different",
                      context.exception.message)
        self.assertEqual(context.exception.code, "1402")
