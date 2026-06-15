import attr

ATTRS_META_APISIX_KEYWORD = "apisix_keyword"

APISIX_MIN_PAGE_SIZE = 10
APISIX_MAX_PAGE_SIZE = 500


def page_size_validation(instance, attributes, value) -> None:
    if value < APISIX_MIN_PAGE_SIZE or value > APISIX_MAX_PAGE_SIZE:
        raise ValueError(f"page_size must be between {APISIX_MIN_PAGE_SIZE} and {APISIX_MAX_PAGE_SIZE}")


@attr.define()
class Pagging:
    page: int = attr.field(converter=int)
    page_size: int = attr.field(converter=int, default=APISIX_MIN_PAGE_SIZE, validator=[page_size_validation])

    @property
    def as_dict(self) -> dict[str, int]:
        return attr.asdict(self)


@attr.define()
class Timeout:
    connect: float
    send: float
    read: float


@attr.define()
class ModifyHeaders:
    add: dict[str, str] | None = attr.field(default=None)
    set_: dict[str, str] | None = attr.field(default=None, metadata={ATTRS_META_APISIX_KEYWORD: "set"})
    remove: list[str] | None = attr.field(default=None)
