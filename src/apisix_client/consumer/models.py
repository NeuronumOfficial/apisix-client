import attrs

from apisix_client.base_models import response_class_factory
from apisix_client.common.converter import str_or_none
from apisix_client.plugin import PluginProtocol


@attrs.define
class Consumer:
    username: str = attrs.field(converter=str)
    group_id: str | None = attrs.field(converter=str_or_none, default=None)
    plugins: list[PluginProtocol] = attrs.field(factory=list)
    desc: str | None = attrs.field(converter=str_or_none, default=None)
    labels: dict | None = attrs.field(default=None)


ConsumerResponse = response_class_factory(Consumer)
