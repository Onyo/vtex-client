# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import BaseClient


ROUTES = {"create": "api/pvt/transactions"}


class TransactionClient(BaseClient):

    def create(self, data):
        """Create an transaction in gateway.

        :param data: dict with basic data of transaction
        :returns: transaction dict
        """
        return self._make_request(ROUTES.get('create'), 'post', data)
