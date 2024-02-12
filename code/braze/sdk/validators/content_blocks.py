from __future__ import annotations  # for Python 3.7–3.9

from annotated_types import Gt
from typing_extensions import NotRequired, TypedDict, Annotated

__all__ = [
    "ContentBlocksInfoParams",
    "ContentBlocksListParams"
]


class ContentBlocksInfoParams(TypedDict):
    content_block_id: str
    include_inclusion_data: NotRequired[bool]


class ContentBlocksListParams(TypedDict):
    modified_after: NotRequired[str]
    modified_before: NotRequired[str]
    limit: NotRequired[Annotated[int, Gt(0)]]
    offset: NotRequired[Annotated[int, Gt(0)]]
