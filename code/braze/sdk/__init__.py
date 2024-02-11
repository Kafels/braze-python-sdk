__all__ = [
    "Braze"
]

import functools
import os
from typing import Optional

from .endpoint import Users


class Braze:

    def __init__(self,
                 token: str,
                 host: Optional[str] = None,
                 timeout: Optional[float] = None):
        self.token = token
        self.host = host or os.environ["BRAZE_HOST"]
        self.timeout = timeout or os.environ.get("BRAZE_TIMEOUT", 30.0)

    @functools.cached_property
    def users(self) -> Users:
        return Users(self)
