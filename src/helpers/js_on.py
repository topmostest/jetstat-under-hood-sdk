def json_encode(obj, **kwargs):
    """Serializes json-string.
    
    Available `kwargs`:
        - skipkeys: bool
        – ensure_ascii: bool
        – check_circular: bool
        – allow_nan: bool
        – cls: type
        – indent: int
        – separators: tuple
        – sort_keys: bool
    :type obj: any
    :return: str
    """
    pass


def json_decode(s, **kwargs):
    """Deserializes json-string.
    
    Available `kwargs`:
        – root_key: str
        – wrap_list: bool
        – encoding: str
        – cls: type
        – object_hook: (any) -> any
        – parse_constant: (any) -> any
        – object_pairs_hook: (any) -> any
    :type s: str
    """
    pass


def json_load(handle, **kwargs):
    """Deserializes json from file.
    
    Available `kwargs`:
        – root_key: str
        – wrap_list: bool
        – encoding: str
        – cls: type
        – object_hook: (any) -> any
        – parse_constant: (any) -> any
        – object_pairs_hook: (any) -> any
    :type handle: typing.IO
    """
    pass


def json_iterate(s, **kwargs):
    """Deserializes json-string on the fly and supplies item-by-item.
    
    Available `kwargs`:
        – encoding: str
        – object_hook: (any) -> any
        – parse_constant: (any) -> any
        – object_pairs_hook: (any) -> any
    :type s: str
    :rtype: typing.Generator
    """
    pass
