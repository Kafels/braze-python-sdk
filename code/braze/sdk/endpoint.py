from __future__ import annotations

import functools
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from . import Braze

__all__ = [
    "Users"
]

from .shared import create_generic_endpoint


class Endpoint:

    def __init__(self, braze: Braze):
        self.braze = braze


class UsersAlias(Endpoint):
    new = create_generic_endpoint(
        doc="https://www.braze.com/docs/api/endpoints/user_data/post_user_alias/",
        endpoint="/users/alias/new",
        method="POST"
    )

    update = create_generic_endpoint(
        doc="https://www.braze.com/docs/api/endpoints/user_data/post_users_alias_update/",
        endpoint="/users/alias/update",
        method="POST"
    )


class UsersExport(Endpoint):
    global_control_group = create_generic_endpoint(
        doc="https://www.braze.com/docs/api/endpoints/export/user_data/post_users_global_control_group/",
        endpoint="/users/export/global_control_group",
        method="POST"
    )

    ids = create_generic_endpoint(
        doc="https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier/",
        endpoint="/users/export/ids",
        method="POST"
    )

    segment = create_generic_endpoint(
        doc="https://www.braze.com/docs/api/endpoints/export/user_data/post_users_segment/",
        endpoint="/users/export/segment",
        method="POST"
    )


class Users(Endpoint):

    @functools.cached_property
    def alias(self):
        return UsersAlias(self.braze)

    @functools.cached_property
    def export(self):
        return UsersExport(self.braze)

    delete = create_generic_endpoint(
        doc="https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/",
        endpoint="/users/delete",
        method="POST"
    )

    identify = create_generic_endpoint(
        doc="https://www.braze.com/docs/api/endpoints/user_data/post_user_identify/",
        endpoint="/users/identify",
        method="POST"
    )

    track = create_generic_endpoint(
        doc="https://www.braze.com/docs/api/endpoints/user_data/post_user_track/",
        endpoint="/users/track",
        method="POST"
    )
