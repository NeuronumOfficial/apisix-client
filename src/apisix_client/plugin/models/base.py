import attrs

from apisix_client.common import ATTRS_META_APISIX_KEYWORD
from apisix_client.plugin.models.authentication import BaseAuth, BaseAuthSetup, KeyAuth, KeyAuthSettings
from apisix_client.plugin.models.observability.loggers import ClickhouseLogger, FileLogger
from apisix_client.plugin.models.security.consumer_restriction import ConsumerRestriction
from apisix_client.plugin.models.traffic import LimitCount, RequestValidation
from apisix_client.plugin.models.transformation import ProxyRewrite, ResponseRewrite


@attrs.define()
class Plugins:
    base_auth: BaseAuth | None = attrs.field(default=None, metadata={ATTRS_META_APISIX_KEYWORD: "basic-auth"})
    base_auth_setup: BaseAuthSetup | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "basic-auth"}
    )
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
    proxy_rewrite: ProxyRewrite | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "proxy-rewrite"}
    )
    response_rewrite: ResponseRewrite | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "response-rewrite"}
    )
    request_validation: RequestValidation | None = attrs.field(
        default=None, metadata={ATTRS_META_APISIX_KEYWORD: "request-validation"}
    )
