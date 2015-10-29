# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import BaseClient


class CardClient(BaseClient):

    def get_information(self, numbers):
        """Get a card information from the first six numbers of the card.

        :param numbers: first six numbers of the card
        :returns: card information
        """
        return self._make_request("api/pvt/bins?code={}".format(numbers), 'get')
