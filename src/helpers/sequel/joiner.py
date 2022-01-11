import helpers.sequel.selector as sql_selector
import helpers.sequel.table as sql_table


class Joiner(sql_selector.Selector):
    def __init__(self, left, kind, right):
        """
        :type left: sql_table.Table
        :type kind: str
        :type right: sql_table.Table
        """
        self._pairs = None
        self._where = None
        self._selected = None

    @property
    def kind(self):
        """Returns kind of join.
        :rtype: str
        """
        pass

    @property
    def target(self):
        """Returns target right table.
        :rtype: sql_table.Table
        """
        pass

    @property
    def case_sense(self):
        """Returns true if join will be performed within case sensitive mode.
        :rtype: bool
        """
        pass

    @case_sense.setter
    def case_sense(self, value):
        """Sets new mode of case sensitive using.
        :type value: bool
        """
        pass

    @property
    def null_around(self):
        """Returns true if joining columns will be prevented from being null.
        :rtype: type
        """
        pass

    @null_around.setter
    def null_around(self, value):
        """Sets new mode of joining columns non-null mode.
        :type value: type
        """
        pass

    def to_sql(self):
        """Returns current statement in sql representation.
        :rtype: str
        """
        pass

    def add_field(self, name, is_left, prefix=None):
        """Adds field to be selected.
        :type name: str
        :type is_left: bool
        :type prefix: str
        :rtype: Joiner
        """
        pass

    def join(self, left, null_left, right, null_right):
        """Adds join pair of fields.
        :type left: str
        :type null_left: bool
        :type right: str
        :type null_right: bool
        :rtype: Joiner
        """
        pass
