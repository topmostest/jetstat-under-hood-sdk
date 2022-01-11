from .number import *
from .string import *
from .js_on import *


LATIN_CHARS = None  # type: list
DIGIT_CHARS = None  # type: list
REPLACE_2_LATIN = None  # type: dict


class DictObj:
    def __init__(self, data):
        """
        :type data: dict
        """
        pass

    def _override_data_at(self, key, value):
        """Sets new value for data at specified key.
        :type key: str
        :type value: any
        """
        pass

    def as_dict(self):
        """Returns whole data in dict representation.
        :rtype: dict
        """
        pass
