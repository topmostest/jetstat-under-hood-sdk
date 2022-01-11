import abc


class Generator:
    def __init__(self, null):
        """
        :type null: int
        """
        pass

    @property
    @abc.abstractmethod
    def type_name(self):
        """Returns type name.
        :rtype: str
        """
        raise NotImplementedError()

    def generate(self):
        """Generates random value or None if chance is non-zero.
                
        """
        pass

    @abc.abstractmethod
    def _generate(self):
        """Generates non-None random value.
                
        """
        raise NotImplementedError()


class BooleanGenerator(Generator):
    def __init__(self, null, **kwargs):
        """Available `kwargs`:
            – chance: int
        :type null: int
        """
        pass

    @property
    def type_name(self):
        """Returns type name.
        :rtype: str
        """
        pass

    def _generate(self):
        """Generates non-None random value.
                
        """
        pass


class DateTimeGenerator(Generator):
    def __init__(self, null, **kwargs):
        """Available `kwargs`:
            – date: bool
            – time: bool
            – min: str
            – max: str
        :type null: int
        """
        pass

    @property
    def type_name(self):
        """Returns type name.
        :rtype: str
        """
        pass

    def _generate(self):
        """Generates non-None random value.
                
        """
        pass


class NumberGenerator(Generator):
    def __init__(self, null, **kwargs):
        """Available `kwargs`:
            – min: float
            – max: float
            – round: int
        :type null: int
        """
        pass

    @property
    def type_name(self):
        """Returns type name.
        :rtype: str
        """
        pass

    def _generate(self):
        """Generates non-None random value.
                
        """
        pass


class OneOfGenerator(Generator):
    def __init__(self, null, **kwargs):
        """Available `kwargs`:
            – items: str
        :type null: int
        """
        pass

    @property
    def type_name(self):
        """Returns type name.
        :rtype: str
        """
        pass

    def _generate(self):
        """Generates non-None random value.
                
        """
        pass


class FakeGenerator(Generator):
    def __init__(self, null, **kwargs):
        """Available `kwargs`:
            – type: str
        :type null: int
        """
        pass

    @property
    def type_name(self):
        """Returns type name.
        :rtype: str
        """
        pass

    def _generate(self):
        """Generates non-None random value.
                
        """
        pass


GENERATORS = None  # type: dict
