from datetime import datetime
from typing import Generic, Iterable, Literal, TypeVar, get_args, get_origin

import attrs
import cattrs

from apisix_client.common import str_or_none
from apisix_client.plugin.models.protocol import PluginProtocol

HTTP_METHODS = Literal[
    "GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE", "PURGE"
]

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


@attrs.define
class BaseSchema:
    name: str | None = attrs.field(default=None, converter=str_or_none)
    desc: str | None = attrs.field(default=None, converter=str_or_none)


V = TypeVar("V")


# https://apisix.apache.org/docs/apisix/admin-api/#v3-new-feature
@attrs.define
class BaseResponse(Generic[V]):
    key: str = attrs.field(converter=str)
    created_index: int = attrs.field(converter=int)
    modified_index: int = attrs.field(converter=int)
    value: V = attrs.field()


# A response from Apisix always contains id, create_time, update_time and others schema specific fields.
# If we want to keep attrs classes with slot=True, we canno't use MixinClass.
def response_class_factory(cls: type) -> type:
    """
    Dynamically creates a new response class based on the given schema specific class `cls`.

    The generated class inherits from `cls` and adds the following fields:
        - id (str): Identifier, converted to string, defaults to an empty string.
        - create_time (datetime): Creation time, converted from a timestamp, defaults to epoch.
        - update_time (datetime): Update time, converted from a timestamp, defaults to epoch.

    The returned class uses attrs, is frozen (immutable), and uses slots for memory efficiency.

    Args:
        cls (type): The base class to inherit from.

    Returns:
        type: A new attrs-based response class with additional fields.
    """
    return attrs.make_class(
        f"Response{cls.__name__}",
        {
            "id": attrs.field(converter=str, default=""),
            "create_time": attrs.field(converter=datetime.fromtimestamp, default=datetime.fromtimestamp(0)),
            "update_time": attrs.field(converter=datetime.fromtimestamp, default=datetime.fromtimestamp(0)),
        },
        bases=(cls,),
        slots=True,
        frozen=True,
    )
