# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import BaseAuthenticatedClient


ROUTES = {"additional-data": "api/pvt/transactions/{}/additional-data",
          "authorize": "api/pvt/transactions/{}/authorization-request",
          "cancel": "api/pvt/transactions/{}/cancellation-request",
          "capture": "api/pvt/transactions/{}/settlement-request",
          "create": "api/pvt/transactions",
          "get": "api/pvt/transactions/{}",
          "payment": "api/pvt/transactions/{}/payments"}


class TransactionClient(BaseAuthenticatedClient):

    def get(self, transaction_id):
        """Get an transaction in gateway.

        :param transaction_id: id of transaction
        :returns: transaction info
        """
        return self._make_request(ROUTES["get"].format(transaction_id),
                                  'get')

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
        return self._make_request(ROUTES["payment"].format(transaction_id),
                                  'get')

    def send_payment(self, transaction_id, data):
        """Send transaction payment to gateway.

        :param transaction_id: id of transaction
        :param data: dict with data of payment
        :returns: payment info
        """
        return self._make_request(ROUTES["payment"].format(transaction_id),
                                  'post',
                                  data)

    def cancel(self, transaction_id, value):
        """Cancel transaction in gateway.

        :param transaction_id: id of transaction
        :param value: amount to be canceled
        :returns: payment info
        """
        data = {"value": value}
        return self._make_request(ROUTES["cancel"].format(transaction_id),
                                  'post',
                                  data)

    def capture(self, transaction_id, value):
        """Capture transaction in gateway.

        :param transaction_id: id of transaction
        :param value: amount to be captured
        :returns: payment info
        """
        data = {"value": value}
        return self._make_request(ROUTES["capture"].format(transaction_id),
                                  'post',
                                  data)

    def send_additional_data(self, transaction_id, data):
        """Send additional data to transaction.

        :param transaction_id: id of transaction
        :param values: additional data payload
        :returns: additional data info
        """
        return self._make_request(
            ROUTES["additional-data"].format(transaction_id), 'post', data)
