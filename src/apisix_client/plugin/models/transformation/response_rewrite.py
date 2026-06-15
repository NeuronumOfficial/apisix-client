from typing import Literal

import attr

from apisix_client.common import ModifyHeaders, bool_or_none, int_or_none, str_or_none

FilterScope = Literal["once", "global"]


@attr.define()
class ResponseFilter:
    regex: str = attr.attr(converter=str)
    replace: str = attr.attr(converter=str)
    scope: FilterScope | None = attr.attr(default=None, converter=str_or_none)
    options: str | None = attr.attr(default=None, converter=str_or_none)


@attr.define()
class ResponseRewrite:
    status_code: int | None = attr.attr(default=None, converter=int_or_none)
    body: str | None = attr.attr(default=None, converter=str_or_none)
    body_base64: bool | None = attr.attr(default=None, converter=bool_or_none)
    headers: ModifyHeaders | None = attr.field(default=None)
    vars: list[list[str]] | None = attr.field(default=None)
    filters: list[ResponseFilter] | None = attr.field(default=None)
