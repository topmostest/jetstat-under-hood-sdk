import helpers.sequel.selector as sql_selector
import helpers.sequel.table as sql_table


class Sorter(sql_selector.Selector):
    def __init__(self, table):
        """
        :type table: sql_table.Table
        """
        self._sort_by = None

    def to_sql(self):
        """Returns current statement in sql representation.
        :rtype: str
        """
        pass

    def add_field(self, name, direction):
        """Add new field for sorting.
        :type name: str
        :type direction: str
        :rtype: Sorter
        """
        pass
