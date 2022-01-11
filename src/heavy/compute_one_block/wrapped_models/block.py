import heavy.compute_one_block.main as compute_main
import heavy.compute_one_block.wrapped_models.contents as contents
import heavy.compute_one_block.wrapped_models.output as output_types
import heavy.compute_one_block.wrapped_models.resulting as resulting
import heavy.compute_one_block.wrapped_models.socket_model as socket_model
import models


class BlockMeta:
    def __init__(self, instance):
        """
        :type instance: models.Block
        """
        pass

    @property
    def identifier(self):
        """Returns block's identifier.
                
        """
        pass

    @property
    def algorithm(self):
        """Returns block's algorithm.
        :rtype: str
        """
        pass

    @property
    def title(self):
        """Returns block's title.
        :rtype: str
        """
        pass

    @property
    def description(self):
        """Returns block's description.
        :rtype: str
        """
        pass


class Parent:
    def __init__(self, meta, parent_index, out_index, in_index, reader):
        """
        :type meta: BlockMeta
        :type parent_index: int
        :type out_index: int
        :type in_index: int
        :type reader: contents.ContentReader
        """
        pass

    @property
    def meta(self):
        """Returns parent block's meta data.
        :rtype: BlockMeta
        """
        pass

    @property
    def parent_index(self):
        """Returns parent list index.
        :rtype: int
        """
        pass

    @property
    def out_index(self):
        """Returns parent's output index.
        :rtype: int
        """
        pass

    @property
    def in_index(self):
        """Returns target's block input index.
        :rtype: int
        """
        pass

    @property
    def contents(self):
        """Returns parent output's content reader.
        :rtype: contents.ContentReader
        """
        pass


class Input(socket_model.Socket):
    def __init__(self, index, *args):
        """Available `args`:
            – dict
        :type index: int
        """
        pass

    def __getitem__(self, index):
        """Returns parent at specified index.
        :type index: int
        :rtype: Parent
        """
        pass

    def __iter__(self):
        """Iterates through parent list.
        :rtype: typing.Generator[Parent]
        """
        pass

    def __len__(self):
        """Returns count of parents.
        :rtype: int
        """
        pass


class Output(socket_model.Socket):
    def __init__(self, block, index, mode, limits, results):
        """
        :type block: models.Block
        :type index: int
        :type mode: str
        :type limits: compute_main.ComputeLimits
        :type results: resulting.Results
        """
        pass

    @property
    def meta(self):
        """Returns current block's meta data.
        :rtype: BlockMeta
        """
        pass

    @property
    def contents(self):
        """Returns target block's output content writer.
        :rtype: contents.ContentWriter
        """
        pass


PREVIEW_WHERE = None  # type: dict
PROCESS_WHERE = None  # type: dict


def pull_predicate(block, index):
    """Returns `pull` predicate of block out contents.
    :type block: models.Block
    :type index: int
    :rtype: (dict) -> typing.Generator[list|dict]
    """
    pass


def aggregate_predicate(block, index):
    """Returns `aggregate` predicate of block out contents.
    :type block: models.Block
    :type index: int
    :rtype: (dict) -> typing.Generator[dict]
    """
    pass


def col_limiter_predicate(limits, results):
    """Returns `col_limiter` predicate of block out contents.
    :type limits: compute_main.ComputeLimits
    :type results: resulting.Results
    :rtype: (int) -> int
    """
    pass


def push_predicate(block, index, meta, mode):
    """Returns `push` predicate of block out contents.
    :type block: models.Block
    :type index: int
    :type meta: output_types.BlockOutputMeta
    :type mode: str
    :rtype: (list) -> any
    """
    pass


def save_predicate(block, index, meta, mode):
    """Returns `save` predicate of block out contents.
    :type block: models.Block
    :type index: int
    :type meta: output_types.BlockOutputMeta
    :type mode: str
    :rtype: () -> any
    """
    pass


def drop_predicate(block, index, meta, mode):
    """Returns `drop` predicate of block out contents.
    :type block: models.Block
    :type index: int
    :type meta: output_types.BlockOutputMeta
    :type mode: str
    :rtype: (list) -> any
    """
    pass
