SUPPORTED = None  # type: list
LINK_SHORTENER_SERVICES = None  # type: list


def parse_url(url):
    """Extracts utm params from url.
    :type url: str
    :rtype: dict
    """
    pass


def replace_value_track(row, utm, track):
    """Replaces utm value track in specified row.
    :type row: dict
    :type utm: str
    :type track: dict
    :rtype: str
    """
    pass


def find_url(ad):
    """Find URLs in ad object
    :type ad: dict
    :rtype: list
    """
    pass


def find_short_link(url):
    """Check given url for short link
    :type url: str
    :rtype: bool
    """
    pass


def get_destination_url(short_url):
    """Get destination URL for given short link
    :type short_url: str
    :rtype: dict
    """
    pass


def unshort_link_with_utm(url, reverse_search=False):
    """Returns destination URL for given shortened url.
    Searches for url in redirect chain that have utm in query string.
    :type url: str
    :type reverse_search: bool
    :rtype: str
    """
    pass
