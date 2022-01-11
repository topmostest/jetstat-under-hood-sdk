class WrongCastError(Exception):
    def __init__(self, col, err):
        """
        :type col: str|int
        :type err: BaseException
        """
        pass

    @property
    def column(self):
        """Returns problematic column name.
        :rtype: str|int
        """
        pass

    @property
    def error(self):
        """Returns original error instance.
        :rtype: BaseException
        """
        pass
