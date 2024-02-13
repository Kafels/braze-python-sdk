from __future__ import annotations  # for Python 3.7–3.9

from typing_extensions import (
    Dict,
    List,
    NotRequired,
    TypedDict, Literal
)

__all__ = [
    "UsersDeleteBody",
    "UsersIdentifyBody",
    "UsersMergeBody",
    "UsersTrackBody"
]


class UsersDeleteBody(TypedDict):
    external_ids: NotRequired[List[str]]
    user_aliases: NotRequired[List[Dict]]
    braze_ids: NotRequired[List[str]]


class UsersIdentifyBody(TypedDict):
    aliases_to_identify: List[Dict]
    merge_behavior: NotRequired[Literal["merge", "none"]]


class UsersMergeBody(TypedDict):
    merge_updates: List[Dict]


class UsersTrackBody(TypedDict):
    attributes: NotRequired[List[Dict]]
    events: NotRequired[List[Dict]]
    purchases: NotRequired[List[Dict]]
