import helpers.sequel.selector as sql_selector
import helpers.sequel.table as sql_table


class Summarizer(sql_selector.Selector):
    def __init__(self, table):
        """
        :type table: sql_table.Table
        """
        self._groups = None
        self._selected = None

    def to_sql(self):
        """Returns current statement in sql representation.
        :rtype: str
        """
        pass

    def add_field(self, name, origin=None, function=None, group=False):
        """Adds field to be selected.
        :type name: str|list
        :type origin: str
        :type function: str
        :type group: bool
        :rtype: Summarizer
        """
        pass
