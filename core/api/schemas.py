from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

from ninja import Schema

from .filters import PaginationOut


TData = TypeVar('TData')
TListItem = TypeVar('TListItem')


class PaginationOut(Schema):
    offset: int
    limit: int
    total: int


class ListPaginatedResponse(Schema, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut


class ApiResponse(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errros: list[Any] = Field(default_factory=list)
