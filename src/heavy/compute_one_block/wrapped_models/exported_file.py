import heavy.compute_one_block.main as compute_main
import heavy.compute_one_block.wrapped_models.contents as contents
import heavy.compute_one_block.wrapped_models.output as output_types
import heavy.compute_one_block.wrapped_models.resulting as resulting
import heavy.compute_one_block.wrapped_models.socket_model as socket_model
import models


class ContentWriter(contents.ContentWriter):
    @property
    def total(self):
        """Returns total row count.
        :rtype: int
        """
        pass

    @total.setter
    def total(self, value):
        """Sets new total row count.
        :type value: int
        """
        pass


class Output(socket_model.Socket):
    def __init__(self, file, _id, limits, results):
        """
        :type file: models.ExportedFile
        :type _id: any
        :type limits: compute_main.ComputeLimits
        :type results: resulting.Results
        """
        pass

    @property
    def reader(self):
        """Returns contents reader.
        :rtype: contents.ContentReader
        """
        pass

    @property
    def writer(self):
        """Returns contents writer.
        :rtype: ContentWriter
        """
        pass


def pull_predicate(file, _id):
    """Returns `pull` predicate of exported file out contents.
    :type file: models.ExportedFile
    :type _id: str
    :rtype: (dict) -> typing.Generator[list|dict]
    """
    pass


def aggregate_predicate(file, _id):
    """Returns `aggregate` predicate of exported file out contents.
    :type file: models.ExportedFile
    :type _id: str
    :rtype: (dict) -> typing.Generator[dict]
    """
    pass


def col_limiter(value):
    """Returns limited count of columns.
    :type value: int
    :rtype: int
    """
    pass


def push_predicate(file, _id, meta):
    """Returns `push` predicate of exported file out contents.
    :type file: models.ExportedFile
    :type _id: str
    :type meta: output_types.ExportedFileOutputMeta
    :rtype: (list) -> any
    """
    pass


def save_predicate(file, _id, meta):
    """Returns `save` predicate of block out contents.
    :type file: models.ExportedFile
    :type _id: str
    :type meta: output_types.ExportedFileOutputMeta
    :rtype: () -> any
    """
    pass


def drop_predicate(file, _id):
    """Returns `drop` predicate of block out contents.
    :type file: models.ExportedFile
    :type _id: str
    :rtype: (list) -> any
    """
    pass
