import attr

from apisix_client.base_models import HTTP_METHODS
from apisix_client.common.converter import int_or_none, str_or_none


@attr.define()
class AllowedByMethods:
    user: str = attr.field(converter=str)
    methods: list[HTTP_METHODS] = attr.field(default=list())


@attr.define()
class ConsumerRestriction:
    whitelist: list[str] = attr.field(default=list())
    blacklist: list[str] = attr.field(default=list())
    rejected_code: int | None = attr.field(converter=int_or_none, default=None)
    rejected_msg: str | None = attr.field(converter=str_or_none, default=None)
    type: str | None = attr.field(converter=str_or_none, default=None)
    allowed_by_methods: list[AllowedByMethods] = attr.field(default=list())
