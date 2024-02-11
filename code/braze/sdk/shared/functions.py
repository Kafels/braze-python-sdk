__all__ = [
    "create_generic_endpoint"
]

import functools
from typing import Optional

import requests

from shared.types import AnyCallableT, DictT
from util import Timber
from .decorator import api

timber = Timber(service="functions")


def create_generic_endpoint(
        function: Optional[AnyCallableT] = None,
        doc: Optional[str] = None,
        endpoint: Optional[str] = None,
        method: Optional[str] = "GET",
):
    @api.inject_call(endpoint=endpoint)
    @functools.wraps(function)
    def impl(_, content: DictT):
        impl.__doc__ = F"Documentation: {doc}"
        return functools.partial(
            requests.request,
            method=method,
            json=content
        )

    return impl
