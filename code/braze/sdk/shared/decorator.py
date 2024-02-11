from __future__ import annotations

from typing import (
    Optional,
    TYPE_CHECKING
)

if TYPE_CHECKING:  # pragma: no cover
    from .endpoint import Endpoint

__all__ = [
    "api"
]

import functools
from datetime import timedelta
from json import loads
from requests import Response

from .auth import BearerAuth
from util import Timber
from shared.types import AnyCallableT


class Api:

    def __init__(self):
        self.timber = Timber(service="api")

    def inject_call(
            self,
            function: Optional[AnyCallableT] = None,
            endpoint: str = None
    ):
        if function is None:
            self.timber.debug("Decorator called with parameters")
            return functools.partial(
                self.inject_call,
                endpoint=endpoint
            )

        @functools.wraps(function)
        def impl(this: Endpoint, *args, **kwargs) -> dict:
            try:
                callable_request: functools.partial = function(this, *args, **kwargs)
                res: Response = callable_request(auth=BearerAuth(this.braze.token),
                                                 url=F"{this.braze.host}{endpoint}",
                                                 timeout=this.braze.timeout)

                self.timber.debug("API response", var={
                    "status_code": res.status_code,
                    "time_elapsed": res.elapsed / timedelta(milliseconds=1),
                    "content": res.content
                })

                res.raise_for_status()
                braze_response = loads(res.content)
                self.timber.debug("Braze response", var={"response": braze_response})

                return braze_response
            except Exception:
                self.timber.exception("An error has occurred while calling braze")
                raise

        return impl


api = Api()
