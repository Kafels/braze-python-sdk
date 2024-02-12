__all__ = [
    "prepare_request"
]

import functools
from typing import Optional

import requests

from shared.types import DictT


def prepare_request(
        content: DictT,
        method: Optional[str] = "GET",
        **kwargs
):
    return functools.partial(
        requests.request,
        method=method,
        json=content,
        **kwargs
    )
