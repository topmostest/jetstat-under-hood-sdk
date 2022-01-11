import helpers.sequel.table as sql_table


class FieldReference:
    def __init__(self, table, name):
        """
        :type table: sql_table.Table
        :type name: str
        """
        self.table = None
        self.name = None

    @property
    def temp_name(self):
        """Returns underlying name of field in current table.
        :rtype: str
        """
        pass


class Expression:
    def __init__(self, *args):
        """Available `args`:
            – str|FieldReference
        """
        self.parts = None


class Join:
    def __init__(self, kind, table):
        """
        :type kind: str
        :type table: sql_table.Table
        """
        self.kind = None
        self.table = None


class OperandCondition:
    def __init__(self, left, operator, right, _and):
        """
        :type left: any
        :type operator: str
        :type right: any
        :type _and: bool
        """
        self.left = None
        self.and_ = None
        self.right = None
        self.operator = None


class ParenthesesCondition:
    def __init__(self, query, _and):
        """
        :type query: any
        :type _and: bool
        """
        self.and_ = None
        self.query = None


class GroupBy:
    def __init__(self):
        """        
        """
        self.fields = None


class OrderBy:
    def __init__(self):
        """        
        """
        self.ascends = None
        self.fields = None


class Limit:
    def __init__(self):
        """        
        """
        self.offset = None
        self.count = None
