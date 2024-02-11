from __future__ import annotations

import functools
from typing import (
    TYPE_CHECKING,
    TypeVar
)

if TYPE_CHECKING:  # pragma: no cover
    from .main import Braze

__all__ = [
    "Endpoint",
    "Users"
]

import requests

from .request import Api

api = Api()
DictT = TypeVar("DictT", bound=dict)


class Endpoint:

    def __init__(self, *, braze: Braze):
        self.braze = braze


class UsersAlias(Endpoint):

    @api.inject_call(endpoint="/users/alias/new")
    def new(
            self,
            content: DictT
    ):
        return functools.partial(
            requests.post,
            json=content
        )


class UsersExport(Endpoint):

    @api.inject_call(endpoint="/users/export/ids")
    def ids(
            self,
            content: DictT
    ):
        return functools.partial(
            requests.post,
            json=content
        )


class Users(Endpoint):

    @functools.cached_property
    def alias(self):
        return UsersAlias(braze=self.braze)

    @functools.cached_property
    def export(self):
        return UsersExport(braze=self.braze)

    @api.inject_call(endpoint="/users/delete")
    def delete(
            self,
            content: DictT
    ):
        return functools.partial(
            requests.post,
            json=content
        )

    @api.inject_call(endpoint="/users/track")
    def track(
            self,
            content: DictT
    ):
        return functools.partial(
            requests.post,
            json=content
        )
