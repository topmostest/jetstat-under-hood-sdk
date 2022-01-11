class MessageBag:
    def __init__(self, threshold):
        """
        :type threshold: int
        """
        self._exceeded = None
        self._messages = None

    def __len__(self):
        """Returns count of collected messages.
        :rtype: int
        """
        pass

    def __iter__(self):
        """Iterates through collected messages.
        :rtype: typing.Generator[str]
        """
        pass

    @property
    def threshold(self):
        """Returns maximal count of messages to be collected.
        :rtype: int
        """
        pass

    @property
    def exceeded(self):
        """Returns count of messages whose exceeded threshold value.
        :rtype: int
        """
        pass

    def push(self, msg):
        """Pushes message to bag or increments exceeded count.
        :type msg: str
        """
        pass
