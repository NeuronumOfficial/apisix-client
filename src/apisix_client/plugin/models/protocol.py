from typing import Protocol, runtime_checkable


@runtime_checkable
class PluginProtocol(Protocol):
    def get_apisix_key(self) -> str: ...
