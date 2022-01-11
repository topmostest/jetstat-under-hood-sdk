import abc


class IterationExceeded(Exception):
    pass


class Timer:
    def __init__(self, counter=0, threshold=0, continuous=True):
        """
        :type counter: int
        :type threshold: int
        :type continuous: bool
        """
        pass

    @property
    def counter(self):
        """Returns counter value.
        :rtype: int
        """
        pass

    @counter.setter
    def counter(self, value):
        """Sets new counter value.
        :type value: int
        """
        pass

    @property
    def threshold(self):
        """Returns threshold value that could not be passed by counter.
        :rtype: int
        """
        pass

    @threshold.setter
    def threshold(self, value):
        """Sets new threshold value that could not be passed by counter.
        :type value: int
        """
        pass

    @property
    def continuous(self):
        """Returns true if counter restarts after threshold has been hit.
        :rtype: bool
        """
        pass

    @continuous.setter
    def continuous(self, value):
        """Sets new mode of counter restarting after threshold has been hit.
        :type value: bool
        """
        pass

    @property
    @abc.abstractmethod
    def next_duration(self):
        """Returns duration of next sleep.
        :rtype: int
        """
        raise NotImplementedError()

    def sleep(self):
        """Sleeps within next duration.
                
        """
        pass


class ExponentialTimer(Timer):
    @property
    def next_duration(self):
        """Returns duration of next sleep.
        :rtype: int
        """
        pass


class LinearTimer(Timer):
    def __init__(self, counter=0, threshold=0, delay=10, continuous=True):
        """
        :type counter: int
        :type threshold: int
        :type delay: int
        :type continuous: bool
        """
        pass

    @property
    def delay(self):
        """Returns fixed delay between sleep iterations.
        :rtype: int
        """
        pass

    @delay.setter
    def delay(self, value):
        """Sets new fixed delay between sleep iterations.
        :type value: int
        """
        pass

    @property
    def next_duration(self):
        """Returns duration of next sleep.
        :rtype: int
        """
        pass


def next_duration(iteration):
    """Returns next time for sleep in exponential backoff mode.
    See: https://developers.google.com/analytics/devguides/config/userdeletion/v3/errors
    :type iteration: int
    :rtype: int
    """
    pass
