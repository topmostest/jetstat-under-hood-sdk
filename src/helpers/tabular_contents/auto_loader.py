import filesystem


def load(fmt, src, **kwargs):
    """Returns reader predicates for tabular data from raw bytes data.
    Available `kwargs`:
        – csv: dict
        – excel: dict
    :type fmt: str
    :type src: str|bytes|filesystem.Path
    :rtype: tuple[() -> int|() -> typing.Generator[tuple[list]]]
    """
    pass
