import abc


class Connector:
    def __init__(self, prefix='', encode=None, decode=None):
        """
        :type prefix: str
        :type encode: (any) -> str
        :type decode: (str) -> any
        """
        pass

    @property
    def prefix(self):
        """Returns key prefix.
        :rtype: str
        """
        pass

    @property
    def encoder(self):
        """Returns encoder function for raw values.
        :return: (any) -> str
        """
        pass

    @property
    def decoder(self):
        """Returns decoder function for raw values.
        :return: (str) -> any
        """
        pass

    @abc.abstractmethod
    def close(self):
        """Closes connection(s) to cache server.
                
        """
        raise NotImplementedError()

    def full_key(self, key):
        """Returns full key of specified one.
        :type key: str
        :rtype: str
        """
        pass

    def get(self, key, default=None):
        """Returns cached value at specified key or `default` in failure case.
        :type key: str
        :type default: any
        """
        pass

    @abc.abstractmethod
    def raw_get(self, key):
        """Returns raw cached value at specified key or raises `KeyError`.
        :type key: str
        """
        raise NotImplementedError()

    def set(self, key, value, expiration=0):
        """Stores value at specified key with specified expiration.
        Returns true on success.
        :type key: str
        :type value: any
        :type expiration: int
        :rtype: bool
        """
        pass

    @abc.abstractmethod
    def raw_set(self, key, value, expiration=0):
        """Stores raw string value at specified key with specified expiration.
        Returns true on success.
        :type key: str
        :type value: any
        :type expiration: int
        :rtype: bool
        """
        raise NotImplementedError()
