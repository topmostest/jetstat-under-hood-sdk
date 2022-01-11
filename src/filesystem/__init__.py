from .path import Path
from .stat import Stat
from .adapters.adapter import Adapter
from .temporary import TempFile


def initialize():
    """Initializes all necessary filesystem-adapters from environment.
        
    """
    pass


def adapter(driver='default'):
    """Returns initialized environment adapter by specified driver name.
    :type driver: name
    :rtype: Adapter
    """
    pass


def temp_file(extension=''):
    """Returns new temporary file.
    Also registers it in temporary basement flow.
    :type extension: str
    :rtype: TempFile
    """
    pass
