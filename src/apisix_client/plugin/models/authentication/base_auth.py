import attrs

from apisix_client.common.converter import bool_or_none, str_or_none


@attrs.define()
class BaseAuth:
    username: str | None = attrs.field(converter=str_or_none, default=None)
    password: str | None = attrs.field(converter=str_or_none, default=None)


@attrs.define()
class RouteBaseAuth:
    hide_credentials: bool | None = attrs.field(converter=bool_or_none, default=None)
    anonymous_consumer: bool | None = attrs.field(converter=bool_or_none, default=None)
