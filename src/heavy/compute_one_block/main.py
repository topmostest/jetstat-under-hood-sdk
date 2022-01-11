import heavy.params as params
import models


class ComputeLimits:
    def __init__(self, data):
        """
        :type data: dict
        """
        self.preview = None
        self.process = None
        self.columns = None


class PaidFeatures:
    def __init__(self, data):
        """
        :type data: list
        """
        self.anti_sampling = None
        self.email_file = None
        self.ga360 = None


class DateRange:
    def __init__(self, data):
        """
        :type data: dict
        """
        self.start = None
        self.finish = None


class Params(params.Params):
    def __init__(self, data):
        """
        :type data: dict
        """
        self.features = None
        self.limit = None
        self.config = None
        self.mode = None
        self.block = None
        self.range = None

    @property
    def resume_poll_key_suffix(self):
        """Returns suffix of caching key to be able to resume polling of current replica.
        :rtype: str
        """
        pass


def perform(operation, parameters):
    """Performs `compute-one-block` job.
    :type operation: models.AsyncOperation
    :type parameters: Params
    :rtype: dict
    """
    pass
