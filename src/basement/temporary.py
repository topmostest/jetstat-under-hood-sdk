import abc


class TemporaryObject:
    def __init__(self):
        """Initialize self.  See help(type(self)) for accurate signature.
        """
        pass

    @property
    def unique_key(self):
        """Returns unique key of temporary object.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def rollback_temp(self):
        """Eliminates temporary object.
                
        """
        raise NotImplementedError()


def register_object(obj):
    """Registers new temporary object at its special key.
    If registry already contains object with its special key previous object will be eliminated.
    :type obj: TemporaryObject
    """
    pass


def drop_object(obj):
    """Drops temporary object from registry and also triggers temporary object's elimination.
    Returns true on success.
    :type obj: TemporaryObject
    :rtype: bool
    """
    pass


def clear():
    """Eliminates all existing in registry temporary objects.
        
    """
    pass
