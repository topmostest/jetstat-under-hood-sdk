import abc


class Caster:
    def __init__(self, **kwargs):
        """Available `kwargs`:
            * none *
        """
        pass

    @abc.abstractmethod
    def cast(self, value):
        """Performs type casting within given value.
        :type value: any
        """
        raise NotImplementedError()


class BooleanCaster(Caster):
    def cast(self, value):
        """Performs type casting within given value.
        :type value: any
        """
        pass


class DateTimeCaster(Caster):
    def __init__(self, **kwargs):
        """Available `kwargs`:
            – format: str
        """
        pass

    @property
    def _default_format(self):
        """Returns default format setting for caster.
        :rtype: str
        """
        pass

    @property
    def _to_fn(self):
        """Returns function from `cast` module to be finally casted.
        :rtype: (any) -> any
        """
        pass

    def cast(self, value):
        """Performs type casting within given value.
        :type value: any
        """
        pass


class DateCaster(DateTimeCaster):
    @property
    def _default_format(self):
        """Returns default format setting for caster.
        :rtype: str
        """
        pass

    @property
    def _to_fn(self):
        """Returns function from `cast` module to be finally casted.
        :rtype: (any) -> any
        """
        pass


class TimeCaster(DateTimeCaster):
    @property
    def _default_format(self):
        """Returns default format setting for caster.
        :rtype: str
        """
        pass

    @property
    def _to_fn(self):
        """Returns function from `cast` module to be finally casted.
        :rtype: (any) -> any
        """
        pass


class NumberCaster(Caster):
    def __init__(self, **kwargs):
        """Available `kwargs`:
            – round: int
        """
        pass

    def cast(self, value):
        """Performs type casting within given value.
        :type value: any
        """
        pass


class StringCaster(Caster):
    def cast(self, value):
        """Performs type casting within given value.
        :type value: any
        """
        pass


CASTERS = None  # type: dict
