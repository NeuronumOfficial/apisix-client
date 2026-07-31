import cattrs
from typing import Iterable, get_args, get_origin
from apisix_client.plugin.models.protocol import PluginProtocol

converter = cattrs.GenConverter()


def unstructure_plugins(plugins: Iterable[PluginProtocol]) -> dict[str, dict]:
    return {plugin.get_apisix_key(): converter.unstructure(plugin) for plugin in plugins}


def is_plugins_collection_type(tp: object) -> bool:
    origin = get_origin(tp)
    if origin not in (list, tuple, set, frozenset, Iterable):
        return False
    args = get_args(tp)
    return len(args) == 1 and args[0] is PluginProtocol


converter.register_unstructure_hook_func(
    is_plugins_collection_type,
    unstructure_plugins,
)
