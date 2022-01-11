import heavy.compute_one_block.wrapped_models.output as output_types


class InternalConverter:
    def __init__(self, output):
        """
        :type output: output_types.OutputMeta
        """
        pass

    @property
    def output(self):
        """Returns output meta.
        :rtype: output_types.OutputMeta
        """
        pass

    @property
    def strict(self):
        """Returns true if failed casting raises errors.
        :rtype: bool
        """
        pass

    @strict.setter
    def strict(self, value):
        """Sets new mode for errors to be raised in failed castings.
        :type value: bool
        """
        pass

    @property
    def dangerous(self):
        """Returns true if dangerous mode is using.
        !!! WARNING !!! don't use it.
        :rtype: bool
        """
        pass

    @dangerous.setter
    def dangerous(self, value):
        """Changes dangerous mode.
        !!! WARNING !!! don't change.
        :type value: bool
        """
        pass

    @property
    def collecting_warnings(self):
        """Returns true if warnings are collecting during type castings.
        :rtype: bool
        """
        pass

    @collecting_warnings.setter
    def collecting_warnings(self, value):
        """Turns ON/OFF warnings collecting.
        :type value: bool
        """
        pass

    @property
    def warnings(self):
        """Returns collected warnings during type casting if this feature is enabled.
        :rtype: dict[str, BaseException]
        """
        pass

    def _to_boolean(self, value):
        """Casts value to boolean.
        :type value: any
        """
        pass

    def _to_date(self, value):
        """Casts value to date.
        :type value: any
        """
        pass

    def _to_datetime(self, value):
        """Casts value to datetime.
        :type value: any
        """
        pass

    def _to_number(self, value):
        """Casts value to number.
        :type value: any
        """
        pass

    def _to_string(self, value):
        """Casts value to string.
        :type value: any
        """
        pass

    def _to_time(self, value):
        """Casts value to time.
        :type value: any
        """
        pass

    def _to_ignore(self, value):
        """Casts value to ignore-type.
        >> Caution: use it carefully.
        >> Ignore-type is special type and could not be used in common blocks.
        :type value: any
        """
        pass

    def cast(self, value, _type, col_name=None):
        """Casts value to specified type.
        :type value: any
        :type _type: str
        :type col_name: str
        """
        pass

    def row_from_dict(self, **kwargs):
        """Returns casted dict-row from dict-row.
        Available `kwargs`:
            *none*
        :rtype: dict
        """
        pass

    def row_from_list(self, *args):
        """Returns casted dict-row from list-row.
        Available `args`:
            *none*
        :rtype: dict
        """
        pass

    def cells_from_dict(self, **kwargs):
        """Returns casted list-row from dict-row.
        Available `kwargs`:
            *none*
        :rtype: list
        """
        pass

    def cells_from_list(self, *args):
        """Returns casted list-row from list-row.
        Available `args`:
            *none*
        :rtype: list
        """
        pass


class StorageConverter(InternalConverter):
    def _to_date(self, value):
        """Casts value to date.
        :type value: any
        """
        pass

    def _to_datetime(self, value):
        """Casts value to datetime.
        :type value: any
        """
        pass

    def _to_time(self, value):
        """Casts value to time.
        :type value: any
        """
        pass
