import heavy.compute_one_block.processors.config as base_config
import heavy.compute_one_block.wrapped_models.block as block
import heavy.compute_one_block.wrapped_models.cells as cells
import heavy.compute_one_block.wrapped_models.contents as contents
import heavy.compute_one_block.wrapped_models.progress as progress
import helpers.filtering.conditions as filter_module
import helpers.metrics as help_metrics
import helpers.sequel.query_builder as sql_query
import helpers.sequel.table as sql_table
import models


class Multiple:
    def __init__(self, data):
        """
        :type data: dict
        """
        pass

    def __len__(self):
        """Returns count of values.
        :rtype: int
        """
        pass

    def __iter__(self):
        """Iterates through value list.
        :rtype: typing.Generator
        """
        pass


class Filter:
    def __init__(self, data):
        """
        :type data: dict
        """
        self.column = None
        self.value = None
        self.operator = None


class SimpleFilter:
    def __init__(self, data):
        """
        :type data: dict
        """
        self.values = None
        self.column = None


class Config(base_config.Config):
    def __init__(self, data):
        """
        :type data: dict
        """
        self.credential = None
        self.filters = None
        self.token = None

    def prepare(self):
        """Performs some preparations before block computing.
                
        """
        pass


class OldStyleConfig(Config):
    def __init__(self, data):
        """
        :type data: dict
        """
        self.all_columns = None


class NewStyleConfig(Config):
    def __init__(self, data):
        """
        :type data: dict
        """
        self.grouping = None
        self.dimensions = None
        self.metrics = None
        self.all_columns = None


class Chunker(contents.PerRowAppender):
    def __init__(self, cast, push, chunk_size=250, pushes_dict=True):
        """
        :type cast: cells.InternalConverter
        :type push: (list) -> any
        :type chunk_size: int
        :type pushes_dict: bool
        """
        pass


def temp_table(**kwargs):
    """Creates temporary sql-table to buffer some kind of data.
    Available `kwargs`:
        – debug_name: str
        – fields: dict
        – types: dict
        – dimensions: list
        – metrics: list
    """
    pass


def join_data(glued, query, progressbar, **kwargs):
    """Performs data joining from specified query to specified temp table.
    Available `kwargs`:
        – left: str
        – right: str
        – process: (dict) -> any
    :type glued: sql_table.Table
    :type query: sql_query.QueryBuilder
    :type progressbar: progress.ComputeProgress
    """
    pass


def compose_data(query, output, progressbar, **kwargs):
    """Finally composes data from temp table to block output.
    Available `kwargs`:
        – pushes_dict: bool
        – decomposed: list[help_metrics.DecomposedMetric]
        – process: (dict) -> any
    :type query: sql_query.QueryBuilder
    :type output: block.Output
    :type progressbar: progress.ComputeProgress
    """
    pass


def refresh_cache(progressbar, credential, action, params=None, entity='campaigns'):
    """Refreshes credential cache via special module.
    :type progressbar: progress.ComputeProgress|None
    :type credential: models.Credential
    :type action: str
    :type params: dict
    :type entity: str
    """
    pass


def looped_replacement(account, idx, count):
    """Returns replacement for loop-type progresses.
    :type account: str
    :type idx: int
    :type count: int
    :rtype: dict
    """
    pass


def joining_replacement(left, right):
    """Returns replacement for join-type progresses.
    :type left: str
    :type right: str
    :rtype: dict
    """
    pass


def date_component(date_str, component, date_str_format=None):
    """Returns dedicated date components from specified date.
    :type date_str: str
    :type component: str
    :type date_str_format: str
    """
    pass


def grouping_table(dimensions, metrics):
    """Creates temporary sql-table for anti-sampling purposes.
    :type dimensions: list
    :type metrics: list
    :rtype: sql_table.Table
    """
    pass


def compose_back(outputs, progressbar, table, flt, metrics, aggregate, pushes_dict=True, **kwargs):
    """Composes back all data into real block output.
    Available `kwargs`:
        – process: (dict) -> any
    :type outputs: list[block.Output]
    :type progressbar: progress.ComputeProgress
    :type table: sql_table.Table
    :type flt: filter_module.Filter|any
    :type metrics: list[help_metrics.DecomposedMetric]
    :type aggregate: (str) -> str
    :type pushes_dict: bool
    """
    pass


def join_entities(
    left_entity,
    left_table,
    right_entity,
    right_table,
    glues,
    merges,
    progressbar,
    **kwargs
):
    """Performs join between temp tables and returns new joined table.
    Available `kwargs`:
        – case_sense: bool
        – null_around: type
    :type left_entity: str
    :type left_table: sql_table.Table
    :type right_entity: str
    :type right_table: sql_table.Table
    :type glues: list
    :type merges: dict|any
    :type progressbar: progress.ComputeProgress
    :rtype: sql_table.Table
    """
    pass


def merge_prefixed(row, cols, prefixes, merges):
    """Returns combined row by prefixed keys.
    :type row: dict
    :type cols: list|tuple
    :type prefixes: list|tuple
    :type merges: dict
    :rtype: dict
    """
    pass
