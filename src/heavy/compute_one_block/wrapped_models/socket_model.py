import heavy.compute_one_block.wrapped_models.output as output_types


class Socket:
    def __init__(self, index):
        """
        :type index: int
        """
        pass

    @property
    def index(self):
        """Returns index of input.
        :rtype: int
        """
        pass


def row_limiter_predicate(mode, limits, results):
    """Returns `row_limiter` predicate of model's out contents.
    :type mode: str
    :type limits: compute_main.ComputeLimits
    :type results: resulting.Results
    :rtype: (int) -> int
    """
    pass


def check_empty_cols(meta):
    """Checks output columns to be non-empty.
    If so pushing will be stopped.
    :type meta: output_types.OutputMeta
    """
    pass
