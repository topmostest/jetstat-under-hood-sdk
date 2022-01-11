import datetime

import heavy.compute_one_block.main as compute_main


class ReportDates:
    def __init__(self, a, b):
        """
        :type a: any
        :type b: any
        """
        pass

    @property
    def start(self):
        """Returns start date from range.
        :rtype: datetime.date
        """
        pass

    @property
    def finish(self):
        """Returns finish date from range.
        :rtype: datetime.date
        """
        pass

    @property
    def length(self):
        """Returns count of dates from range.
        :rtype: int
        """
        pass

    def __iter__(self):
        """Iterates through dates from range.
        :rtype: typing.Generator[datetime.date]
        """
        pass


class Ranges:
    def __init__(self, dates, compute, features):
        """
        :type dates: ReportDates
        :type compute: compute_main.ComputeLimits
        :type features: compute_main.PaidFeatures
        """
        pass

    @property
    def dates(self):
        """Returns date range.
        :rtype: ReportDates
        """
        pass

    @property
    def compute(self):
        """Returns compute limits.
        :rtype: compute_main.ComputeLimits
        """
        pass

    @property
    def features(self):
        """Returns paid feature list.
        :rtype: compute_main.PaidFeatures
        """
        pass
