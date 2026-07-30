from typing import Literal

import attrs

from apisix_client.common import bool_or_none, int_or_none, str_or_none

LimitCountPolicy = Literal["local", "redis", "redis-cluster"]


@attrs.define
class LimitCountRule:
    count: int = attrs.field(converter=int)
    time_window: int = attrs.field(converter=int)
    key: str = attrs.field(converter=str)
    header_prefix: str | None = attrs.field(converter=str_or_none, default=None)


@attrs.define
class LimitCount:
    count: int = attrs.field(converter=int)
    time_window: int = attrs.field(converter=int)
    key: str | None = attrs.field(converter=str_or_none, default=None)
    key_type: str | None = attrs.field(converter=str_or_none, default=None)
    rejected_code: int = attrs.field(converter=int, default=503)
    rejected_msg: str | None = attrs.field(converter=str_or_none, default=None)
    rules: list[LimitCountRule] | None = attrs.field(default=None)
    policy: LimitCountPolicy | None = attrs.field(converter=str_or_none, default=None)
    allow_degradation: bool | None = attrs.field(converter=bool_or_none, default=None)
    show_limit_quota_header: bool | None = attrs.field(converter=bool_or_none, default=None)
    group: str | None = attrs.field(converter=str_or_none, default=None)
    redis_host: str | None = attrs.field(converter=str_or_none, default=None)
    redis_port: int | None = attrs.field(converter=int_or_none, default=None)
    redis_username: str | None = attrs.field(converter=str_or_none, default=None)
    redis_password: str | None = attrs.field(converter=str_or_none, default=None)
    redis_ssl: bool | None = attrs.field(converter=bool_or_none, default=None)
    redis_ssl_verify: bool | None = attrs.field(converter=bool_or_none, default=None)
    redis_database: int | None = attrs.field(converter=int_or_none, default=None)
    redis_keepalive_timeout: int | None = attrs.field(converter=int_or_none, default=None)
    redis_keepalive_pool: int | None = attrs.field(converter=int_or_none, default=None)
    redis_cluster_nodes: list[str] | None = attrs.field(default=None)
    redis_cluster_name: str | None = attrs.field(converter=str_or_none, default=None)
    redis_cluster_ssl: bool | None = attrs.field(converter=bool_or_none, default=None)
    redis_cluster_ssl_verify: bool | None = attrs.field(converter=bool_or_none, default=None)

    @staticmethod
    def get_apisix_key() -> str:
        return "limit-count"
