import helpers.sequel.expression as sql_expr
import helpers.sequel.table as sql_table


SELECT = 0
COUNT = 1
DELETE = 2
ARG_MASK = '¡!§¶•{}•¶§!¡'


class QueryBuilder:
    def __init__(self):
        """        
        """
        self._parent = None
        self._limit = None
        self._select = None
        self._aliases = None
        self._tables = None
        self._order_by = None
        self._having = None
        self._first_table = None
        self._where = None
        self._group_by = None
        self._args = None
        self._joins = None
        self._ons = None

    def economy(self):
        """Closes all using tables if necessary.
        Attention (!!!): Use it only for transaction economy purposes.
        """
        pass

    def __str__(self):
        """Compiles query string.
        :rtype: str
        """
        pass

    def __iter__(self):
        """Iterates through selection query response.
        :rtype: typing.Generator
        """
        pass

    def __len__(self):
        """Queries all count of potential query.
        :rtype: int
        """
        pass

    def delete(self):
        """Queries row deletion within collected conditions.
        Returns count of affected rows.
        :rtype: int
        """
        pass

    def select(self, alias=None, **kwargs):
        """Adds field to selection.
        Available `kwargs`:
            * none *
        :type alias: str
        :rtype: QueryBuilder
        """
        pass

    def from_(self, table):
        """Adds table from where selection will be performed.
        :type table: sql_table.Table
        :rtype: QueryBuilder
        """
        pass

    def join(self, kind, table):
        """Adds another table to be joined.
        :rtype: QueryBuilder
        """
        pass

    def on(self, *args, _and=True, idx=-1):
        """Adds "on"-type condition for join-clause.
        Available `args`:
            * none *
        :type _and: bool
        :type idx: int
        :rtype: QueryBuilder
        """
        pass

    def group_by(self, **kwargs):
        """Adds "group by"-type clause.
        Available `kwargs`:
            * none *
        :rtype: QueryBuilder
        """
        pass

    def order_by(self, ascending=True, **kwargs):
        """Adds "order by"-type clause.
        Available `kwargs`:
            * none *
        :rtype: QueryBuilder
        """
        pass

    def where(self, *args, _and=True):
        """Adds "where"-type clause.
        Available `args`:
            * none *
        :type _and: bool
        :rtype: QueryBuilder
        """
        pass

    def having(self, *args, _and=True):
        """Adds "having"-type clause.
        Available `args`:
            * none *
        :type _and: bool
        :rtype: QueryBuilder
        """
        pass

    def limit(self, offset=None, count=None):
        """Adds limit-type clause.
        :type offset: int
        :type count: int
        :rtype: QueryBuilder
        """
        pass

    def _get_table(self, table):
        """Adds specified table to set and returns specified table or first from set.
        :type table: sql_table.Table
        :rtype: sql_table.Table
        """
        pass

    def _register_arg(self, value):
        """Registers argument value to supply it separately near sql-string.
        Returns placeholder string instead.
        :type value: any
        :rtype: typing.Generator[str]
        """
        pass

    def _expression(self, **kwargs):
        """Returns expression instance from given arguments.
        Available `kwargs`:
            – parts: list
            – value: any
            – function: str
            – table: sql_table.Table
            – name: str
        """
        pass

    def _condition(self, output, *args, _and=True, left_ref=True, right_ref=True):
        """Resolves condition-based arguments and returns necessary instance.
        Available `args`:
            * none *
        :type output: list
        :type _and: bool
        :type left_ref: bool
        :type right_ref: bool
        """
        pass

    def _operand(self, value, scalar_as_reference):
        """Resolves conditional operand.
        :type value: any
        :type scalar_as_reference: bool
        """
        pass

    def _fetch(self, _type=SELECT):
        """Executes current query and fetches all its data from response.
        :type _type: int
        :rtype: typing.Generator
        """
        pass

    def _compile_args(self, sql, args, _type):
        """Replaces in SQL-query certain constructions by arguments.
        Also prepares argument dictionary for transaction supplying.
        :type sql: str
        :type args: dict
        :type _type: int
        :rtype: tuple[str|tuple|dict]
        """
        pass

    def _sql(self, _type=SELECT):
        """Compiles query from current collected info.
        :type _type: int
        :rtype: str
        """
        pass

    def _sub_sql(self):
        """Compiles query part in case of sub-query instance.
        :rtype: str
        """
        pass

    def _ref2sql(self, field):
        """Returns selection field reference's string representation as SQL-part.
        :type field: sql_expr.FieldReference
        :rtype: str
        """
        pass

    def _expr2sql(self, expr, **kwargs):
        """Returns selection field expression's string representation as SQL-part.
        Available `kwargs`:
            – alias: str
            – ascending: bool
        :type expr: sql_expr.Expression
        :rtype: str
        """
        pass

    def _join2sql(self, join, ons):
        """Returns join's string representation as SQL-part.
        :type join: sql_expr.Join
        :type ons: list[sql_expr.Condition]
        :rtype: str
        """
        pass

    def _condition2sql(self, idx, count, condition):
        """Returns condition's string representation as SQL-part.
        :type idx: int
        :type count: int
        :type condition: sql_expr.OperandCondition|sql_expr.ParenthesesCondition
        :rtype: str
        """
        pass

    def _limit2sql(self, offset, count):
        """Returns limit's string representation as SQL-part.
        :type offset: int
        :type count: int
        :rtype: str
        """
        pass
