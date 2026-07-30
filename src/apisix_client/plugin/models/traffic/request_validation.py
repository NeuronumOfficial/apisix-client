from typing import Any, Literal

import attr
import jsonschema

from apisix_client.common import bool_or_none, int_or_none, str_or_none

JsonSchemaType = Literal["string", "integer", "number", "boolean", "array", "object", "null"]


@attr.define()
class RequestPropertySchema:
    """Represents a single JSON Schema property definition."""

    type: JsonSchemaType | None = attr.field(default=None)
    pattern: str | None = attr.field(default=None, converter=str_or_none)
    enum: list[Any] | None = attr.field(default=None)
    default: Any = attr.field(default=None)
    minimum: int | float | None = attr.field(default=None)
    maximum: int | float | None = attr.field(default=None)
    min_length: int | None = attr.field(default=None, converter=int_or_none, alias="minLength")
    max_length: int | None = attr.field(default=None, converter=int_or_none, alias="maxLength")
    min_items: int | None = attr.field(default=None, converter=int_or_none, alias="minItems")
    max_items: int | None = attr.field(default=None, converter=int_or_none, alias="maxItems")
    items: "RequestPropertySchema | None" = attr.field(default=None)
    unique_items: bool | None = attr.field(default=None, converter=bool_or_none, alias="uniqueItems")

    def to_dict(self) -> dict[str, Any]:
        _key_map = {
            "type": "type",
            "pattern": "pattern",
            "enum": "enum",
            "default": "default",
            "minimum": "minimum",
            "maximum": "maximum",
            "min_length": "minLength",
            "max_length": "maxLength",
            "min_items": "minItems",
            "max_items": "maxItems",
            "unique_items": "uniqueItems",
        }
        result: dict[str, Any] = {}
        for py_name, json_name in _key_map.items():
            val = getattr(self, py_name)
            if val is not None:
                result[json_name] = val
        if self.items is not None:
            result["items"] = self.items.to_dict()
        return result


@attr.define()
class RequestValidationSchema:
    """Top-level JSON Schema object used for header_schema / body_schema validation."""

    properties: dict[str, RequestPropertySchema] | None = attr.field(default=None)
    required: list[str] | None = attr.field(default=None)
    type: Literal["object"] = attr.field(default="object")

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {"type": self.type}
        if self.required is not None:
            result["required"] = self.required
        if self.properties is not None:
            result["properties"] = {k: v.to_dict() for k, v in self.properties.items()}
        return result


def _validate_schema(
    instance: object, attribute: attr.Attribute, value: RequestValidationSchema | None
) -> None:
    if value is None:
        return
    schema_dict = value.to_dict()
    try:
        validator_cls = jsonschema.validators.validator_for(schema_dict)
        validator_cls.check_schema(schema_dict)
    except jsonschema.exceptions.SchemaError as e:
        raise ValueError(f"Invalid JSON schema for '{attribute.name}': {e.message}") from e


@attr.define()
class RequestValidation:
    header_schema: RequestValidationSchema | None = attr.field(default=None, validator=[_validate_schema])
    body_schema: RequestValidationSchema | None = attr.field(default=None, validator=[_validate_schema])
    rejected_code: int | None = attr.field(default=None, converter=int_or_none)
    rejected_msg: str | None = attr.field(default=None)

    def __attrs_post_init__(self) -> None:
        if self.header_schema is None and self.body_schema is None:
            raise ValueError("At least one of 'header_schema' or 'body_schema' must be provided.")

    @staticmethod
    def get_apisix_key() -> str:
        return "request-validation"
