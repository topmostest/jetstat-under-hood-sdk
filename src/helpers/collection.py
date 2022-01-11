def has(coll, path):
    """Returns true if dot-notated path exists in collection.
    :type coll: list|tuple|dict
    :type path: str
    :rtype: bool
    """
    pass


def get(coll, path, default=None):
    """Returns value from collection at dot-notated nested path.
    :type coll: list|tuple|dict
    :type path: str
    :type default: any
    """
    pass


def pull(coll, path, default=None):
    """Returns value from collection at dot-notated nested path.
    If path exists key at last nest level will be deleted.
    :type coll: list|tuple|dict
    :type path: str
    :type default: any
    """
    pass


def chunk(coll, size):
    """Splits collection by chunks with specified chunk size.
    :type coll: list|tuple
    :type size: int
    :rtype: typing.Generator[list|tuple]
    """
    pass


def index_of(coll, predicate):
    """Returns first index of element that matches by predicate.
    If not found returns -1.
    :type coll: list|tuple
    :type predicate: (any) -> bool
    :rtype: int
    """
    pass


def find(coll, predicate):
    """Returns first element that matches by predicate.
    If not found returns None.
    :type coll: list|tuple
    :type predicate: (any) -> bool
    """
    pass


def merge(predicate, *args):
    """Merges two lists by primary key predicate.
    Available `args`:
        – list|tuple
    :type predicate: (any) -> str
    :rtype: list
    """
    pass


def unnest_dict(indict, pre=None):
    """Recursive generator for converting given dictionary to flat lists.
    :type indict: dict
    :type pre: list
    :rtype: typing.Generator
    """
    pass


def flatten_dict(indict):
    """Makes dict flat.
    :type indict: dict
    :rtype: dict
    """
    pass
