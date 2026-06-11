import attr

from apisix_client.base_models import HTTP_METHODS
from apisix_client.common.converter import str_or_none


@attr.define()
class ModifyHeaders:
    add: dict[str, str] | None = attr.field(default=None)
    set_: dict[str, str] | None = attr.field(default=None, metadata={"ATTRS_META_APISIX_KEYWORD": "set"})
    remove: list[str] | None = attr.field(default=None)


@attr.define()
class ProxyRewrite:
    uri: str | None = attr.field(converter=str_or_none, default=None)
    method: HTTP_METHODS | None = attr.field(converter=str_or_none, default=None)
    regex_uri: list[str] | None = attr.field(default=None)
    host: str | None = attr.field(converter=str_or_none, default=None)
    headers: ModifyHeaders | None = attr.field(default=None)
