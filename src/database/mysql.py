import mysql.connector as mysql_connector
import mysql.connector.cursor as mysql_cursor

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
        self.client.autocommit = None

    @property
    def client(self):
        """Returns mongodb client.
        :rtype: mysql_connector.MySQLConnection
        """
        pass

    def close(self):
        """Closes current connection.
                
        """
        pass


class Transaction(database.Transaction):
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
        :rtype: mysql_cursor.MySQLCursor
        """
        pass

    def _open_cursor(self, server_side_name=None):
        """Opens new cursor.
        :type server_side_name: str
        :rtype: mysql_cursor.MySQLCursor
        """
        pass

    def _close_cursor(self):
        """Closes current cursor.
                
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
