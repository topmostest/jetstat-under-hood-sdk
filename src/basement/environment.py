import os


PRODUCTION = 'production'
DEVELOPMENT = 'development'
LOCAL = 'local'
NAME = None


def load():
    """Loads all environment variables from `.env` file into `os.environ` storage.
        
    """
    pass


def get(key, default='', decode=None):
    """Returns value of specified environment variable.
    Returns default value if variable with specified key doesn't exist.
    :type key: str
    :type default: str
    :type decode: (str) -> any
    """
    pass
