import attrs


@attrs.define()
class Timeout:
    connect: float
    send: float
    read: float
