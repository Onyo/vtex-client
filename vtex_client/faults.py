# -*- coding: utf-8 -*-
"""
Module with specific Exceptions raised by Clients.
"""
from __future__ import unicode_literals


class BaseClientError(BaseException):

    """
    All VTEX errors contains an error code and message, we use this
    constructor to handle this information.
    """

    def __init__(self, message, code=None):
        self.message = message
        self.code = code


class AuthorizationError(BaseClientError):

    """An authentication error in the API."""

    pass


class InvalidDataError(BaseClientError):

    """An BadRequest error in the API."""

    pass


class GetewayError(BaseClientError):

    """An internal gateway error in the API."""

    pass
