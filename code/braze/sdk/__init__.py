__all__ = [
    "Braze"
]

import functools

from .endpoint import Users


class Braze:

    def __init__(
            self,
            host: str,
            token: str
    ):
        self.token = token
        self.host = host

    @functools.cached_property
    def users(self) -> Users:
        return Users(self)
