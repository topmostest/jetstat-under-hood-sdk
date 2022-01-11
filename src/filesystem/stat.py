import helpers


class Stat(helpers.DictObj):
    def __init__(self, **kwargs):
        """Available `kwargs`:
            – mime: str
            – size: int
        """
        pass

    @property
    def mime(self):
        """Returns mime-type.
        :rtype: str
        """
        pass

    @property
    def size(self):
        """Returns size in bytes.
        :rtype: int
        """
        pass
