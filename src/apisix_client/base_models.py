from typing import Generic, TypeVar

import attrs
import cattrs

converter = cattrs.GenConverter()

converter.register_structure_hook(lambda x, cls: cls.fromtimestamp(x))
converter.register_structure_hook(lambda x: int(x.timestamp()))


def strip_empty_fields_unstructure_hook(cls):
    def remove_empty_values(d):
        cleaned_dict = {}
        for k, v in d.items():
            if isinstance(v, dict) and v:
                cleaned_v = remove_empty_values(v)
                if cleaned_v:
                    cleaned_dict[k] = cleaned_v
            elif isinstance(v, (list, tuple, set)) and not v:
                continue
            elif v not in (None, ""):
                cleaned_dict[k] = v
        return cleaned_dict

    def strip_empty_fields(obj):
        primitive = converter.unstructure_attrs_asdict(obj)
        if "plugins" in primitive:
            plugins_dict = {}
            for plugin in obj.plugins:
                plugins_dict[plugin.apisix_key_name()] = converter.unstructure_attrs_asdict(plugin)

            primitive["plugins"] = plugins_dict

        return remove_empty_values(primitive)

    return strip_empty_fields


def all_attrs_class_predicate(obj):
    return hasattr(obj, "__attrs_attrs__")


converter.register_unstructure_hook_factory(all_attrs_class_predicate, strip_empty_fields_unstructure_hook)


V = TypeVar("V")
T = TypeVar("T")


@attrs.define()
class BaseResponse(Generic[V]):
    key: str
    created_index: int = attrs.field(converter=int)
    modified_index: int = attrs.field(converter=int)
    value: V = attrs.field()
