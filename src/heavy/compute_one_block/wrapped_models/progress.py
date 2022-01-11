import helpers


class ComputeProgress(helpers.DictObj):
    def __init__(self, operation, block, store_steps):
        """
        :type operation: str
        :type block: str
        :type store_steps: int
        """
        pass

    @property
    def internal_type(self):
        """Returns internal type.
        :rtype: str
        """
        pass

    @property
    def current(self):
        """Returns current value.
        :rtype: int
        """
        pass

    @property
    def goal(self):
        """Returns goal value.
        :rtype: int
        """
        pass

    def set(self, _type=None, current=None, goal=None, replace=None, **kwargs):
        """Sets new progress data.
        Available `kwargs`:
            * none *
        :type _type: str
        :type current: int
        :type goal: int
        :type replace: dict
        """
        pass

    def set_default(self, _type, current=None, replace=None, **kwargs):
        """Sets new progress type with default values.
        Available `kwargs`:
            * none *
        :type _type: str
        :type current: int
        :type replace: dict
        """
        pass

    def increment_always(self):
        """Increments progress without store steps logic.
                
        """
        pass

    def increment_stepped(self):
        """Increments progress with store steps logic.
                
        """
        pass

    def increment_default(self):
        """Increments both current and goal values of progress.
                
        """
        pass


def create(operation, block, mode):
    """Creates new progress instance.
    :type operation: str
    :type block: str
    :type mode: str
    :rtype: ComputeProgress
    """
    pass
