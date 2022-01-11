class Error(Exception):
    pass


class NotFoundError(Error):
    pass


class BadColumnError(Error):
    pass


class EmptyContentsError(Error):
    pass


class WrongContentsError(Error):
    pass


class MicrolangError(Error):
    pass


class ColumnTypeError(Error):
    pass


class ExternalServiceError(Error):
    pass
