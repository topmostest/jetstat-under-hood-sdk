import models
import models.repositories.mongodb as repository


class Repository(repository.Repository):
    def __init__(self, mask, *args):
        """Available `args`:
            – %index%: any
        :type mask: str
        """
        pass

    @property
    def _model_ctor(self):
        """Returns covered model constructor.
        :rtype: type[models.Model]
        """
        pass

    @property
    def _timestamps(self):
        """Returns true if covered models use standard timestamps.
        :rtype: bool
        """
        pass

    @property
    def _connector_name(self):
        """Returns mongodb connector name.
        :rtype: str
        """
        pass

    @property
    def _collection_name(self):
        """Returns collection name.
        :rtype: str
        """
        pass

    @property
    def _wrap_id_where(self):
        """Returns true if repository specially wraps id condition in future queries.
        :rtype: bool
        """
        pass

    @property
    def _additional_query_filter_params(self):
        """Returns additional params for each query in cache models.
        :rtype: dict
        """
        pass

    def _wrap_where(self, where, with_related=True):
        """Wraps filter part of future query.
        :type where: any
        :type with_related: bool
        """
        pass

    def pull(self, **kwargs):
        """Enumerates all models from collection in raw view.
        Available `kwargs`:
            – where: dict
            – offset: int
            – order: tuple
        :rtype: typing.Generator[dict]
        """
        pass

    def push(self, rows):
        """Inserts many records of model into collection in raw view.
        :type rows: list
        """
        pass

    def destroy(self):
        """Drops collection of current repository.
                
        """
        pass
