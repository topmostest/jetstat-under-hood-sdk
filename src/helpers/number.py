def number(value):
    """Converts specified value to float or to int if no fraction remained.
    :type value: any
    :rtype: float|int
    """
    pass


def enumerate_chunks(chunk_size, total_size):
    """Iterates through chunks.
    :type chunk_size: int
    :type total_size: int
    :rtype: typing.Generator[tuple[int]]
    """
    pass


def indexed_round(value, threshold, count, decimals=None):
    """Rounds given value and returns it with prefix index that's restricted by index count.
    :type value: float
    :type threshold: float
    :type count: int
    :type decimals: int
    :rtype: tuple[float|int, int]
    """
    pass


def leading_zeros(value, max_length, zero='0'):
    """Returns numeric value within leading zeros (or something else specified).
    :type value: int|float
    :type max_length: int
    :type zero: str
    :rtype: str
    """
    pass
