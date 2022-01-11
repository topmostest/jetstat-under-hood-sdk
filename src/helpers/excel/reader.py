import filesystem


class Worksheet:
    def __init__(self, path, index, cell):
        """
        :type path: filesystem.Path
        :type index: int|str
        :type cell: str
        """
        pass

    @property
    def length(self):
        """Returns row count of reading worksheet.
        :rtype: int
        """
        pass

    def __enter__(self):
        """Ability to use `with` statement.
        :rtype: Worksheet
        """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ability to exit from `with` statement.
        :type exc_type: type[BaseException]
        :type exc_val: str
        :type exc_tb: traceback
        """
        pass

    def __iter__(self):
        """Iterates through worksheet's rows.
        :rtype: typing.Generator[list]
        """
        pass
