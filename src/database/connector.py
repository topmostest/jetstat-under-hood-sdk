import abc


class Connector:
    def __init__(self, host, port, db_name, options=None, username=None, password=None, **kwargs):
        """Available `kwargs`:
            * none *
        :type host: str
        :type port: int
        :type db_name: str
        :type options: dict
        :type username: str
        :type password: str
        """
        pass

    @abc.abstractmethod
    def close(self):
        """Closes current connection.
                
        """
        raise NotImplementedError()


class Transaction:
    def __init__(self, connector):
        """
        :type connector: Connector
        """
        pass

    def __enter__(self):
        """Ability to use `with` statement.
        :rtype: Transaction
        """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ability to exit from `with` statement.
        :type exc_type: type[BaseException]
        :type exc_val: str
        :type exc_tb: traceback
        """
        pass

    @property
    def _connector(self):
        """Returns connector instance.
        :rtype: Connector
        """
        pass

    @property
    def _cursor(self):
        """Returns cursor instance.
                
        """
        pass

    @property
    def active(self):
        """Returns true if transaction is in progress.
        :rtype: bool
        """
        pass

    @abc.abstractmethod
    def _open_cursor(self, server_side_name=None):
        """Opens new cursor.
        :type server_side_name: str
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def _close_cursor(self):
        """Closes current cursor.
                
        """
        raise NotImplementedError()

    def start(self):
        """Starts new transaction.
        Returns true if transaction was really started.
        :rtype: bool
        """
        pass

    def close(self):
        """Closes current transaction.
        Returns true if transaction was really closed.
        :rtype: bool
        """
        pass

    def _wrap(self, method, *args, **kwargs):
        """Wraps call to catch errors and close transaction properly.
        In succeeded case returns response from given method.
        Available `args`:
            * none *
        Available `kwargs`:
            * none *
        :type method: callable
        """
        pass

    def execute(self, *args, **kwargs):
        """Executes any query.
        Available `args`:
            * none *
        Available `kwargs`:
            – _server_side_cursor: bool
            – _method: str
        """
        pass

    def fetchmany(self, count=1000):
        """Fetches results from current cursor.
        :type count: int
        """
        pass

    @abc.abstractmethod
    def _fetch(self, count):
        """Fetches results from current cursor.
        :type count: int
        """
        raise NotImplementedError()

    def fetch_to_end(self, count=1000):
        """Fetches results until end from current cursor.
        :type count: int
        """
        pass

    def rowcount(self):
        """Returns count of rows affected from latest query.
        :rtype: int
        """
        pass

    def description(self):
        """Returns column description from latest query.
        :rtype: list
        """
        pass

    @abc.abstractmethod
    def escape(self, ident):
        """Returns escaped identifier.
        :type ident: str
        :rtype: str
        """
        raise NotImplementedError()
