# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import BaseClient


ROUTES = {"create": "api/pvt/transactions",
          "authorize": "api/pvt/transactions/{}/authorization-request",
          "get_payment": "api/pvt/transactions/{}/payments"}


class TransactionClient(BaseClient):

    def create(self, data):
        """Create an transaction in gateway.

        :param data: dict with basic data of transaction
        :returns: transaction dict
        """
        return self._make_request(ROUTES.get('create'), 'post', data)

    def authorize(self, transaction_id, data):
        """Authorize an transaction in gateway.

        :param transaction_id: id of transaction
        :param data: dict with basic data of transaction
        :returns: authorization info
        """
        return self._make_request(ROUTES["authorize"].format(transaction_id),
                                  'post',
                                  data)

    def get_payment(self, transaction_id):
        """Create an transaction in gateway.

        :param transaction_id: id of transaction
        :returns: payment info
        """
        return self._make_request(ROUTES["get_payment"].format(transaction_id),
                                  'get',
                                  {})
