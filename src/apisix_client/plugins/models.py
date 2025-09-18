import attrs


@attrs.define()
class KeyAuth:
    key: str = attrs.field()

    @classmethod
    def apisix_key_name(cls) -> str:
        return "key-auth"


@attrs.define()
class LimitCount:
    count: int = attrs.field()
    time_window: int = attrs.field()
    key: str = attrs.field()
    key_type: str = attrs.field()
    rejected_code: int = attrs.field(default=503)
    policy: str = attrs.field(default="")
    allow_degradation: bool | None = attrs.field(default=None)
    show_limit_quota_header: bool | None = attrs.field(default=None)

    @classmethod
    def apisix_key_name(cls) -> str:
        return "limit-count"


PluginTypes = KeyAuth | LimitCount
