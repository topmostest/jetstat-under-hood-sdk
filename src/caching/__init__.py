from .connector import Connector
from .enc_dec import encode as default_encode
from .enc_dec import decode as default_decode


def initialize():
    """Initializes all necessary cache connectors.
        
    """
    pass


def connector(driver='default'):
    """Returns initialized environment connector with specified driver name.
    :type driver: str
    :rtype: Connector
    """
    pass


def finalize():
    """Finalizes all initialized environment connectors.
        
    """
    pass
