import psycopg2.pool as pgpool

import database


class Connector(database.Connector):
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

    @property
    def pool(self):
        """Returns postgres connection pool.
        :rtype: pgpool.SimpleConnectionPool
        """
        pass

    def close(self):
        """Closes current connection.
                
        """
        pass


class Transaction(database.Transaction):
    def __init__(self, connector):
        """
        :type connector: Connector
        """
        pass

    @property
    def _connector(self):
        """Returns connector instance.
        :rtype: Connector
        """
        pass

    @property
    def _connection(self):
        """Returns acquired connection instance.
        :rtype: pgpool.Connection
        """
        pass

    @property
    def _cursor(self):
        """Returns cursor instance.
        :rtype: pgpool.Cursor
        """
        pass

    @property
    def active(self):
        """Returns true if transaction is in progress.
        :rtype: bool
        """
        pass

    def _open_cursor(self, server_side_name=None):
        """Opens new cursor.
        :type server_side_name: str
        :rtype: pgpool.Cursor
        """
        pass

    def _close_cursor(self):
        """Closes current cursor.
                
        """
        pass

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

    def execute(self, *args, **kwargs):
        """Executes any query.
        Available `args`:
            * none *
        Available `kwargs`:
            – _method: str
        """
        pass

    def _fetch(self, count):
        """Fetches results from current cursor.
        :type count: int
        """
        pass

    def escape(self, ident):
        """Returns escaped identifier.
        :type ident: str
        :rtype: str
        """
        pass
