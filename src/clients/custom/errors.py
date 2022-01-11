class JsonError(Exception):
    def __init__(self, data, **kwargs):
        """Available `kwargs`:
            – code: str
            – text: str
        :type data: dict
        """
        pass

    def __getattr__(self, key):
        """Magic attribute by map.
        :type key: str
        """
        pass
