import helpers.sequel.selector as sql_selector
import helpers.sequel.table as sql_table


class UniversalSelector(sql_selector.Selector):
    def __init__(self, table, sql, *args, **kwargs):
        """Available `args`:
            * none *
        Available `kwargs`:
            – _append: bool
        :type table: sql_table.Table
        :type sql: str
        """
        pass

    def to_sql(self):
        """Returns current statement in sql representation.
        :rtype: str
        """
        pass
