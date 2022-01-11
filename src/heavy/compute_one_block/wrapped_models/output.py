import helpers


class OutputMeta(helpers.DictObj):
    def __init__(self, data):
        """
        :type data: dict
        """
        pass

    @property
    def column_names(self):
        """Returns column names.
        :rtype: list[str]
        """
        pass

    @property
    def column_types(self):
        """Returns column types.
        :rtype: list[str]
        """
        pass

    @property
    def no_column_duplicates(self):
        """Returns true if output doesn't support column duplicates.
        :rtype: bool
        """
        pass

    @no_column_duplicates.setter
    def no_column_duplicates(self, value):
        """Sets new behaviour for column duplicates.
        :type value: bool
        """
        pass

    @property
    def columns(self):
        """Returns column key-values where key is name and value is type.
        :rtype: list[tuple[str]]
        """
        pass

    @columns.setter
    def columns(self, value):
        """Sets new column key-values.
        :type value: list[tuple[str]]
        """
        pass

    @property
    def total(self):
        """Returns total row count.
        :rtype: int
        """
        pass

    @total.setter
    def total(self, value):
        """Sets new total row count.
        :type value: int
        """
        pass

    @property
    def column_count(self):
        """Returns count of columns.
        :rtype: int
        """
        pass

    def additional(self, key, value):
        """Sets additional data to meta.
        :type key: str
        :type value: any
        """
        pass

    def as_dict(self):
        """Returns whole data in dict representation.
        :rtype: dict
        """
        pass


class BlockOutputMeta(OutputMeta):
    def __init__(self, data):
        """
        :type data: dict
        """
        pass

    @property
    def index(self):
        """Returns index of block output.
        :rtype: int
        """
        pass

    @property
    def title(self):
        """Returns title of block output.
        :rtype: str
        """
        pass


class ExportedFileOutputMeta(OutputMeta):
    def __init__(self, data):
        """
        :type data: dict
        """
        pass

    @property
    def identifier(self):
        """Returns identifier of exported file output.
        :rtype: str
        """
        pass
