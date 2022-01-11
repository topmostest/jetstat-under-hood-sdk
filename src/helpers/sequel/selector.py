import helpers.sequel.statement_based as stmt
import helpers.sequel.table as sql_table


class Selector(stmt.StatementBased):
    def __init__(self, table):
        """
        :type table: sql_table.Table
        """
        self._length = None
        self._origins = None
        self._mode_counting = None
        self._aliases = None

    def __iter__(self):
        """Iterates through table records.
        :rtype: typing.Generator[dict|list|int]
        """
        pass

    def __len__(self):
        """Returns count of records from table.
        :rtype: int
        """
        pass

    def _add_origin_field(self, name):
        """Adds field that will be selected and will use origin name in iteration.
        :type name: str
        """
        pass
