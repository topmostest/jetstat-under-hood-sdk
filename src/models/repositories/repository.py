import abc

import models


class Repository:
    def __init__(self):
        """        
        """
        pass

    @property
    @abc.abstractmethod
    def _model_ctor(self):
        """Returns covered model constructor.
        :rtype: type[models.Model]
        """
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def _primary_key(self):
        """Returns primary key name.
        :rtype: str
        """
        raise NotImplementedError()

    @property
    def _timestamps(self):
        """Returns true if covered models use standard timestamps.
        :rtype: bool
        """
        pass

    def related_with(self, model, model_key='id', foreign_key=''):
        """Adds relation with another model for queries.
        :type model: models.Model
        :type model_key: str
        :type foreign_key: str
        :rtype: Repository
        """
        pass

    def _wrap_where(self, where, with_related=True):
        """Wraps filter part of future query.
        :type where: any
        :type with_related: bool
        """
        pass

    def search(self, where=None, **kwargs):
        """Searches for models.
        
        Available `kwargs`:
            * none *
        :type where: any
        :rtype: typing.Generator[models.Model]
        """
        pass

    @abc.abstractmethod
    def _search(self, where, **kwargs):
        """Searches for models (storage level).
        
        Available `kwargs`:
            * none *
        :type where: any
        :return: typing.Generator[dict]
        """
        raise NotImplementedError()

    def one(self, id_where=None, or_fail=True, **kwargs):
        """Returns first occurrence of model searching.
        
        Available `kwargs`:
            * none *
        :type id_where: any
        :type or_fail: bool
        :rtype: models.Model
        """
        pass

    def aggregate(self, where=None, function='count', columns=None):
        """Performs aggregate query.
        :type where: any
        :type function: str
        :type columns: list
        """
        pass

    @abc.abstractmethod
    def _aggregate(self, where, function, columns):
        """Performs aggregate query (storage level).
        :type where: any
        :type function: str
        :type columns: list
        """
        raise NotImplementedError()

    def create(self, attributes=None):
        """Creates new one model and stores it into storage.
        :type attributes: dict
        :rtype: models.Model
        """
        pass

    @abc.abstractmethod
    def _create(self, attributes):
        """Creates new one model and stores it into storage (storage level).
        :type attributes: dict
        :rtype: dict
        """
        raise NotImplementedError()

    def edit(self, model, attributes=None):
        """Updates specified model in storage.
        :type model: entities.Model
        :type attributes: dict
        :rtype: bool
        """
        pass

    @abc.abstractmethod
    def _edit(self, model):
        """Updates specified model in storage (storage level).
        :type model: models.Model
        :rtype: bool
        """
        raise NotImplementedError()

    def update(self, where=None, attributes=None):
        """Massive updates models in storage.
        :type where: any
        :type attributes: dict
        :rtype: int
        """
        pass

    @abc.abstractmethod
    def _update(self, where, attributes):
        """Massive updates models in storage (storage level).
        :type where: any
        :type attributes: dict
        :rtype: int
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, model):
        """Deletes specified model from storage.
        :type model: models.Model
        :rtype: bool
        """
        raise NotImplementedError()

    def drop(self, where=None):
        """Massive deletes models from storage.
        :type where: any
        :rtype: int
        """
        pass

    @abc.abstractmethod
    def _drop(self, where):
        """Massive deletes models from storage (storage level).
        :type where: any
        :rtype: int
        """
        raise NotImplementedError()
