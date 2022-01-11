def detect(
    reader,
    include_head=True,
    forced_types=None,
    exclude_types=None,
    auto_type_row_count=50,
    end=None
):
    """Detects tabular content headings and data types.
    VANGA MODE ON
    :type reader: typing.Generator[list]
    :type include_head: bool
    :type forced_types: list
    :type exclude_types: list|tuple
    :type auto_type_row_count: int
    :type end: (list) -> bool
    :rtype: typing.Generator[tuple[list]]
    """
    pass
