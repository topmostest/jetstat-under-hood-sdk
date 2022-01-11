import heavy.compute_one_block.wrapped_models.cells as cells
import heavy.compute_one_block.wrapped_models.output as output_types


class Contents:
    def __init__(self, output, converter):
        """
        :type output: output_types.OutputMeta
        :type converter: type[cells.InternalConverter]
        """
        self._output = None
        self._cast = None

    @property
    def column_names(self):
        """Returns column names.
        :rtype: list[str]
        """
        pass

    @property
    def column_types(self):
        """Returns column types.
        :rtype: list[str]
        """
        pass

    @property
    def columns(self):
        """Returns column key-values where key is name and value is type.
        :rtype: list[tuple[str]]
        """
        pass

    @columns.setter
    def columns(self, value):
        """Sets new column key-values.
        :type value: list[tuple[str]]
        """
        pass

    @property
    def total(self):
        """Returns total row count.
        :rtype: int
        """
        pass

    @property
    def column_count(self):
        """Returns count of columns.
        :rtype: int
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

    def additional(self, key, value):
        """Sets additional data to output.
        :type key: str
        :type value: any
        """
        pass


class ContentReader(Contents):
    def __init__(self, output, pull, aggregate, pulls_dict):
        """
        :type output: output_types.OutputMeta
        :type pull: (dict) -> typing.Generator[dict|list]
        :type aggregate: (dict) -> typing.Generator[dict]
        :type pulls_dict: bool
        """
        self._pull = None
        self._aggregate = None
        self._pulls_dict = None

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

    def pull_row(self, **kwargs):
        """Pulls each row from contents.
        Available `kwargs`:
            – where: dict
            – offset: int
            – sort: tuple
        :rtype: typing.Generator[dict]
        """
        pass

    def pull_cells(self, **kwargs):
        """Pulls each row from contents as cell list.
        Available `kwargs`:
            – where: dict
            – offset: int
            – sort: tuple
        :rtype: typing.Generator[list]
        """
        pass

    def aggregate(self, **kwargs):
        """Performs aggregation against contents.
        Available `kwargs`:
            – where: dict
            – function: dict
            – columns: dict
        :rtype: typing.Generator[dict]
        """
        pass


class ContentWriter(Contents):
    def __init__(self, output, col_limiter, chunk_size, row_limiter, pushes_dict, push, save, drop):
        """
        :type output: output_types.OutputMeta
        :type col_limiter: (int) -> int
        :type chunk_size: int
        :type row_limiter: (int) -> int
        :type pushes_dict: bool
        :type push: (list) -> any
        :type save: () -> any
        :type drop: () -> any
        """
        self._push = None
        self._col_limiter = None
        self._drop = None
        self._row_limiter = None
        self._pushes_dict = None
        self._chunk_size = None
        self._save = None

    @property
    def no_column_duplicates(self):
        """Returns true if output doesn't support column duplicates.
        :rtype: bool
        """
        pass

    @no_column_duplicates.setter
    def no_column_duplicates(self, value):
        """Sets new behaviour for column duplicates.
        :type value: bool
        """
        pass

    @property
    def columns(self):
        """Returns column key-values where key is name and value is type.
        :rtype: list[tuple[str]]
        """
        pass

    @columns.setter
    def columns(self, value):
        """Sets new column key-values.
        :type value: list[tuple[str]]
        """
        pass

    def per_row_appender(self):
        """Returns new per row appender.
        :rtype: PerRowAppender
        """
        pass

    def clear(self):
        """Drops all contents and resets output meta info.
                
        """
        pass


class PerRowAppender:
    def __init__(self, chunk_size, cast, pushes_dict, get_total, set_total, limiter, push, save):
        """
        :type chunk_size: int
        :type cast: cells.InternalConverter
        :type pushes_dict: bool
        :type get_total: () -> int
        :type set_total: (int) -> any
        :type limiter: (int) -> int
        :type push: (list) -> any
        :type save: () -> any
        """
        pass

    @property
    def chunk_size(self):
        """Returns chunk size.
        :rtype: int
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
    def ignore(self):
        """Returns true if appending rows are needed to be passed through ignore filter.
        :rtype: bool
        """
        pass

    @ignore.setter
    def ignore(self, value):
        """Sets mode for appending rows those are needed to be passed through ignore filter.
        :type value: bool
        """
        pass

    def __enter__(self):
        """Ability to use `with` statement.
        :rtype: PerRowAppender
        """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ability to exit from `with` statement.
        :type exc_type: type[BaseException]
        :type exc_val: str
        :type exc_tb: traceback
        """
        pass

    def push_row(self, row):
        """Pushes row to contents.
        Raises `InterruptedError` on failure.
        :type row: dict
        """
        pass

    def push_cells(self, cell_list):
        """Pushes cells to content.
        Raises `InterruptedError` on failure.
        :type cell_list: list
        """
        pass

    def save(self):
        """Flushes remained rows and saves meta information.
                
        """
        pass
