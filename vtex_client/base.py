# -*- coding: utf-8 -*-
"""
Module with common functions used in all Clients
"""
from __future__ import unicode_literals

import json
import requests
from . import faults


class BaseClient(object):

    """Base client for VTEX webservice"""

    api_url = "https://api.vtexpayments.com.br/{}"

    def _get_headers(self):
        return {'CONTENT-TYPE': 'application/json'}

    def _handle_error(self, response):
        status = response.status_code
        response_data = response.json()
        if 'error' in response_data:
            error_message = response_data['error']['message']
            error_code = response_data['error']['code']
        elif 'Message' in response_data:
            error_message = response_data['Message']
            error_code = None
        else:
            raise KeyError("Response does not contain the expected errorkeys")

        if status == 400:
            raise faults.InvalidDataError(error_message, error_code)
        elif status in (401, 403):
            raise faults.AuthorizationError(error_message, error_code)
        elif status == 500:
            raise faults.GetewayError(error_message, error_code)
        else:
            raise ValueError("{} is a invalid status code".format(status))

    def _make_url(self, url_sufix):
        return self.api_url.format(url_sufix)

    def _make_request(self, url_sufix, method, data=None):
        """Send a request to gateway and handles error responses.

        :param url_sufix: Endpoint url
        :param method: HTTP verb used in request
        :param data: Data to be sent to gateway
        :returns: Loaded JSON response of request
        """
        if not data:
            data = {}

        url = self._make_url(url_sufix)
        response = getattr(requests, method)(url,
                                             data=json.dumps(data),
                                             headers=self._get_headers())

        if response.status_code != 200:
            return self._handle_error(response)

        return response.json() if response.text else {}


class BaseAuthenticatedClient(BaseClient):

    """Base authenticated client for VTEX webservice"""

    api_url = "https://{}.vtexpayments.com.br/{}"

    def __init__(self, api_store, api_key, api_token):
        self.api_store = api_store
        self.api_key = api_key
        self.api_token = api_token

    def _make_url(self, url_sufix):
        return self.api_url.format(self.api_store, url_sufix)

    def _get_headers(self):
        headers = super(BaseAuthenticatedClient, self)._get_headers()
        headers.update({'X-VTEX-API-APPKEY': self.api_key,
                        'X-VTEX-API-APPTOKEN': self.api_token})
        return headers
