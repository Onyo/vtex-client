# -*- coding: utf-8 -*-
"""
Module with common functions used in all Clients
"""
from __future__ import unicode_literals

import json
import logging
import re
import requests

from . import faults


logger = logging.getLogger('vtex-client')


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

    def _get_cleaned_data(self, data):
        """Remove sensitive data to be sent to logging"""
        data = json.dumps(data)
        data = re.sub('"validationCode":[ ]?((\"\d+\")?(\d+)?)',
                      '"validationCode": "XXX"',
                      data)
        return data

    def _log(self, url, method, data, response=None, exception=None):
        lines = []
        data = self._get_cleaned_data(data)
        if response:
            lines.append("HTTP/1.1 {} {}".format(response.status_code,
                                                 response.reason))
            lines.append("Location: {} {}".format(method, url))
            for key, value in response.headers.items():
                lines.append("{}: {}".format(key, value))
            lines.append("Request Body:")
            lines.append(data)
            lines.append("Respose Body:")
            lines.append(response.text)
        else:
            lines.append("{} {} HTTP/1.1".format(method, url))
            lines.append("Location: {}".format("url"))
            lines.append("Request Body:")
            lines.append(data)

        if exception:
            lines.append("Exception: {} {}".format(exception.__class__,
                                                   exception.message))

        content = "\n".join(lines)
        logger.debug(content)

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

        headers = self._get_headers()
        url = self._make_url(url_sufix)
        log_data = {"url": url,
                    "method": method.upper(),
                    "data": data}

        self._log(**log_data)
        try:
            response = getattr(requests, method)(url,
                                                 data=json.dumps(data),
                                                 headers=headers)
        except Exception as error:
            log_data["exception"] = error
            self._log(**log_data)
            raise error

        log_data["response"] = response
        self._log(**log_data)

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
