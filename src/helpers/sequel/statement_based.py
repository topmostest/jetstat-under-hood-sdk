import abc

import helpers.sequel.table as sql_table


class StatementBased:
    def __init__(self, table):
        """
        :type table: sql_table.Table
        """
        pass

    @property
    def table(self):
        """Returns table instance.
        :rtype: sql_table.Table
        """
        pass

    def __enter__(self):
        """Ability to use `with` statement.
        :rtype: StatementBased
        """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ability to exit from `with` statement.
        :type exc_type: type[BaseException]
        :type exc_val: str
        :type exc_tb: traceback
        """
        pass

    @abc.abstractmethod
    def to_sql(self):
        """Returns current statement in sql representation.
        :rtype: str
        """
        raise NotImplementedError()

    def _select(self):
        """Selects table records.
        :rtype: typing.Generator[list]
        """
        pass


def temp_name(table, name):
    """Returns temporary field name.
    :type table: sql_table.Table
    :type name: str
    :rtype: str
    """
    pass


def full_name(table, name):
    """Returns full field name.
    :type table: sql_table.Table
    :type name: str
    :rtype: str
    """
    pass
