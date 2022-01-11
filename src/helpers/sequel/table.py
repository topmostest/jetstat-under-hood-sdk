import basement.temporary as temporary
import database.pgsql as pgsql


class Table(temporary.TemporaryObject):
    def __init__(self, connector=None, name=None):
        """
        :type connector: pgsql.Connector
        :type name: str
        """
        pass

    @property
    def connector(self):
        """Returns sql-database connector.
        :rtype: pgsql.Connector
        """
        pass

    @property
    def transaction(self):
        """Returns transaction instance to perform queries.
        :rtype: pgsql.Transaction
        """
        pass

    @property
    def created(self):
        """Returns true if table is created.
        :rtype: bool
        """
        pass

    @property
    def name(self):
        """Returns name of temporary table.
        :rtype: str
        """
        pass

    @property
    def original_fields(self):
        """Returns original field names.
        :rtype: list
        """
        pass

    @property
    def fields(self):
        """Returns temporary field names.
        :rtype: list
        """
        pass

    @property
    def types(self):
        """Returns type names of fields.
        :rtype: list
        """
        pass

    def add_field(self, name, _type):
        """Adds new field to table.
        :type name: str
        :type _type: str
        :rtype: Table
        """
        pass

    def boolean(self, name):
        """Adds new field of type `boolean`.
        :type name: str
        :rtype: Table
        """
        pass

    def date(self, name):
        """Adds new field of type `date`.
        :type name: str
        :rtype: Table
        """
        pass

    def datetime(self, name):
        """Adds new field of type `datetime`.
        :type name: str
        :rtype: Table
        """
        pass

    def number(self, name):
        """Adds new field of type `number`.
        :type name: str
        :rtype: Table
        """
        pass

    def string(self, name):
        """Adds new field of type `string`.
        :type name: str
        :rtype: Table
        """
        pass

    def time(self, name):
        """Adds new field of type `time`.
        :type name: str
        :rtype: Table
        """
        pass

    def create(self):
        """Creates table in sql-database.
                
        """
        pass

    def insert(self):
        """Returns inserter instance.
                
        """
        pass

    def query(self):
        """Returns query builder instance.
                
        """
        pass

    def joiner(self, kind, target):
        """Returns joiner instance.
        :type kind: str
        :type target: Table
        """
        pass

    def sorter(self):
        """Returns sorter instance.
                
        """
        pass

    def summarizer(self):
        """Returns summarizer instance.
                
        """
        pass

    def universal_selector(self, sql, *args, **kwargs):
        """Returns summarizer instance.
        Available `args`:
            * none *
        Available `kwargs`:
            – _append: bool
        :type sql: str
        """
        pass

    def rollback_temp(self):
        """Eliminates temporary object.
                
        """
        pass
