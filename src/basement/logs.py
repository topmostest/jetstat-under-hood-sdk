import logging


ANNOYING_LOGGERS = None  # type: tuple


def logger():
    """Returns main app's logger instance.
    :rtype: logging.Logger
    """
    pass


def debug(msg, *args, **kwargs):
    """Log message within DEBUG level.
    Available `args`: *none*
    Available `kwargs`: *none*
    :type msg: any
    """
    pass


def info(msg, *args, **kwargs):
    """Log message within INFO level.
    Available `args`: *none*
    Available `kwargs`: *none*
    :type msg: any
    """
    pass


def warning(msg, *args, **kwargs):
    """Log message within WARNING level.
    Available `args`: *none*
    Available `kwargs`: *none*
    :type msg: any
    """
    pass


def error(msg, *args, **kwargs):
    """Log message within ERROR level.
    Available `args`: *none*
    Available `kwargs`:
        – exc_info: bool
    :type msg: any
    """
    pass


def critical(msg, *args, **kwargs):
    """Log message within CRITICAL level.
    Also notifies about error to external service (Bugsnag).
    Available `args`: *none*
    Available `kwargs`:
        – exc_info: bool
        – variables: dict
    :type msg: any
    """
    pass
