import abc


class Model:
    def __init__(self, **kwargs):
        """Available `kwargs`:
            – %attribute%: any
        """
        pass

    @property
    def _strict_schema(self):
        """Returns true if model uses strict schema mode.
        :rtype: bool
        """
        pass

    @abc.abstractmethod
    def _defaults(self):
        """Returns default values for initial model state.
        This method also defines schema for current model.
        :rtype: dict
        """
        raise NotImplementedError()

    def _raw_get(self, key):
        """Returns attributes value.
        If key not found `KeyError` will be risen.
        :type key: str
        """
        pass

    def _raw_set(self, key, value):
        """Sets attribute value.
        If key not found `KeyError` will be risen (only in strict schema mode).
        :type key: str
        :type value: any
        """
        pass

    def get(self, key, default=None):
        """Returns attribute value at specified key or `default` if key not found.
        :type key: str
        :type default: any
        """
        pass

    def set(self, key, value):
        """Sets new value of attribute at specified key.
        If key not found `KeyError` will be risen (only in strict schema mode).
        :type key: str
        :type value: any
        :rtype: Model
        """
        pass

    def export(self, origin=False):
        """Returns all attributes as entire dict.
        If `origin` is true attributes will be present directly from attribute storage "as-is".
        :type origin: bool
        :rtype: dict
        """
        pass

    def fill(self, **kwargs):
        """Sets massive attributes from `kwargs` dict.
        Available `kwargs`:
            – %attribute%: any
        :rtype: Model
        """
        pass

    def __getitem__(self, key):
        """Magic attribute getter.
        :type key: str
        """
        pass

    def __setitem__(self, key, value):
        """Magic attribute setter.
        :type key: str
        :type value: any
        """
        pass
