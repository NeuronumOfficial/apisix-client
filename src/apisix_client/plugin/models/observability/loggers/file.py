import attr


@attr.define()
class FileLogger:
    path: str = attr.field(converter=str)
    log_format: dict | None = attr.field(default=None)
    include_req_body: bool | None = attr.field(converter=bool, default=False)
    include_req_body_expr: list | None = attr.field(default=None)
    include_resp_body: bool | None = attr.field(converter=bool, default=False)
    include_resp_body_expr: list | None = attr.field(default=None)
    match: list[list] | None = attr.field(default=None)
