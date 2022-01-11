import helpers.sequel.statement_based as stmt
import helpers.sequel.table as sql_table


class Inserter(stmt.StatementBased):
    def __init__(self, table, length):
        """
        :type table: sql_table.Table
        :type length: int
        """
        self._length = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ability to exit from `with` statement.
        :type exc_type: type[BaseException]
        :type exc_val: str
        :type exc_tb: traceback
        """
        pass

    def to_sql(self):
        """Returns current statement in sql representation.
        :rtype: str
        """
        pass

    def push(self, row):
        """Inserts one row.
        :type row: dict
        :rtype: Inserter
        """
        pass

    def flush(self):
        """Really inserts buffered rows into db.
                
        """
        pass
