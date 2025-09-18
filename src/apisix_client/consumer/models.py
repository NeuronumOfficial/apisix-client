from datetime import datetime
from typing import Dict, List

import attrs

from apisix_client.plugins import PluginTypes


@attrs.define()
class ConsumerResponse:
    create_time: datetime = attrs.field(converter=datetime.fromtimestamp)
    update_time: datetime = attrs.field(converter=datetime.fromtimestamp)
    username: str = attrs.field(converter=str)
    desc: str = attrs.field(converter=str, default="")
    plugins: Dict[str, PluginTypes] = attrs.field(default={})


@attrs.define()
class Consumer:
    username: str = attrs.field(converter=str)
    group_id: str = attrs.field(default="", converter=str)
    plugins: List[PluginTypes] = attrs.field(default=[])
    desc: str = attrs.field(default="", converter=str)
    labels: dict = attrs.field(default={})
