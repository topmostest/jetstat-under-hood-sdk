import datetime


MASK_ANY = '*'
MASK_YEAR = 'Y'
MASK_MONTH = 'M'
MASK_DAY = 'D'
MASK_HOUR = 'h'
MASK_MINUTE = 'm'
MASK_SECOND = 's'
ALL_MASKS = None  # type: tuple
DATE_MASKS = None  # type: tuple
TIME_MASKS = None  # type: tuple


def parse(value, fmt):
    """Parses date and time components from given value and within given format.
    :type value: any
    :type fmt: str
    :rtype: datetime.datetime
    """
    pass


def fulfill_year(value):
    """Fulfills year value if it's less than 1000.
    :type value: int
    :rtype: int
    """
    pass


def date_range(a, b):
    """Returns all dates between date-a and date-b.
    :type a: datetime.date
    :type b: datetime.date
    :rtype: typing.Generator
    """
    pass


MASK_WEEKDAY = 'W'
MASK_WEEKNUM = 'w'
MASK_AMPM = 'H'
OUTPUT_MASKS = None  # type: dict


def to_format(date, fmt, locale=None):
    """Formats specified date using both given format and language.
    NOTE!!! This function is developed for certain purposes => USE strftime instead.
    :type date: datetime.datetime
    :type fmt: str
    :type locale: str
    :rtype: str
    """
    pass


def get_name(number, kind, locale=None, mode=0):
    """Returns name of specified kind of date-part.
    Modes are:
        – 0: short
        – 1: full/infinitive case
        – 2: full/relative case
    :type number: int
    :type kind: str
    :type locale: str
    :type mode: int
    :rtype: str
    """
    pass


def boundary(value, start, component):
    """Returns start/end of specified date/time within given component.
    Components are:
        – 0: of second (not supported)
        – 1: of minute
        – 2: of hour
        – 3: of day
        – 4: of week
        – 5: of month
        – 6: of year
    :type value: datetime.date|datetime.datetime|datetime.time
    :type start: bool
    :type component: int
    :rtype: datetime.date|datetime.datetime|datetime.time
    """
    pass
