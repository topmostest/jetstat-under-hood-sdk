import pymongo
import pymongo.database as db

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
    def client(self):
        """Returns mongodb client.
        :rtype: pymongo.MongoClient
        """
        pass

    @property
    def database(self):
        """Returns selected default database.
        :rtype: db.Database
        """
        pass

    def close(self):
        """Closes current connection.
                
        """
        pass
