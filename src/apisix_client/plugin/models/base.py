import attrs

from apisix_client.common import ATTRS_META_APISIX_KEYWORD
from apisix_client.plugin.models.authentication import BaseAuth, KeyAuth, KeyAuthSettings, RouteBaseAuth
from apisix_client.plugin.models.observability.loggers import ClickhouseLogger, FileLogger
from apisix_client.plugin.models.security.consumer_restriction import ConsumerRestriction
from apisix_client.plugin.models.traffic.limit_count import LimitCount


@attrs.define()
class BasePlugins:
    key_auth: KeyAuth | KeyAuthSettings | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "key-auth"}
    )
    limit_count: LimitCount | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "limit-count"}
    )
    clickhouse_logger: ClickhouseLogger | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "clickhouse-logger"}
    )
    file_logger: FileLogger | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "file-logger"}
    )
    consumer_restriction: ConsumerRestriction | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "consumer-restriction"}
    )


@attrs.define()
class Plugins(BasePlugins):
    base_auth: BaseAuth | RouteBaseAuth | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "basic-auth"}
    )


@attrs.define()
class RoutePlugins(BasePlugins):
    base_auth: RouteBaseAuth | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "basic-auth"}
    )
