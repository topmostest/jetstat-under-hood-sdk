import filesystem


def load(src, reader_options=None):
    """Returns reader predicates for tabular data in csv format.
    :type src: str|bytes|filesystem.Path
    :type reader_options: dict
    :rtype: tuple[() -> int|() -> typing.Generator[dict]]
    """
    pass
