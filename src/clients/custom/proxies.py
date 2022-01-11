class ProxySelector:
    def __init__(self):
        """        
        """
        pass

    @property
    def loaded(self):
        """Returns true if proxy settings were loaded from environment.
        :rtype: bool
        """
        pass

    @property
    def host(self):
        """Returns last selected host.
        :rtype: str
        """
        pass

    @property
    def port(self):
        """Returns proxy port.
        :rtype: int
        """
        pass

    @property
    def user(self):
        """Returns proxy user name.
        :rtype: str
        """
        pass

    @property
    def password(self):
        """Returns proxy server password.
        :rtype: str
        """
        pass

    def re_select(self):
        """Re-selects proxy host from pool of hosts.
        :rtype: ProxySelector
        """
        pass

    def __str__(self):
        """Returns raw proxy connection string without scheme.
        :rtype: str
        """
        pass

    def __iter__(self):
        """Iterates through scheme associations.
        :rtype: typing.Generator[tuple]
        """
        pass


def selector():
    """Returns proxy selector instance.
    :rtype: ProxySelector
    """
    pass
