import abc

import pymongo.collection as mongo_collection

import database.mongodb as mongodb
import models


class Repository(models.ModelRepository):
    def __init__(self):
        """        
        """
        pass

    @property
    def _connector_name(self):
        """Returns mongodb connector name.
        :rtype: str
        """
        pass

    @property
    def connector(self):
        """Returns mongodb connector instance.
        :rtype: mongodb.Connector
        """
        pass

    @property
    @abc.abstractmethod
    def _collection_name(self):
        """Returns collection name.
        :rtype: str
        """
        raise NotImplementedError()

    @property
    def collection(self):
        """Returns collection instance.
        :rtype: mongo_collection.Collection
        """
        pass

    @property
    def _primary_key(self):
        """Returns primary key name.
        :rtype: str
        """
        pass

    @property
    def _wrap_id_where(self):
        """Returns true if repository specially wraps id condition in future queries.
        :rtype: bool
        """
        pass

    def _wrap_where(self, where, with_related=True):
        """Wraps filter part of future query.
        :type where: any
        :type with_related: bool
        """
        pass

    def _search(self, where, **kwargs):
        """Searches for models (storage level).
        
        Available `kwargs`:
            – offset: int
            - order: tuple
        :type where: any
        :return: typing.Generator[dict]
        """
        pass

    def _aggregate(self, where, function, columns):
        """Performs aggregate query (storage level).
        :type where: any
        :type function: str
        :type columns: list
        """
        pass

    def _create(self, attributes):
        """Creates new one model and stores it into storage (storage level).
        :type attributes: dict
        :rtype: dict
        """
        pass

    def _prepare_model_before_query(self, model):
        """Prepares model attributes before db-level query.
        :type model: models.Model
        :rtype: (dict, dict)
        """
        pass

    def _edit(self, model):
        """Updates specified model in storage (storage level).
        :type model: models.Model
        :rtype: bool
        """
        pass

    def _update(self, where, attributes):
        """Massive updates models in storage (storage level).
        :type where: any
        :type attributes: dict
        :rtype: int
        """
        pass

    def delete(self, model):
        """Deletes specified model from storage.
        :type model: models.Model
        :rtype: bool
        """
        pass

    def _drop(self, where):
        """Massive deletes models from storage (storage level).
        :type where: any
        :rtype: int
        """
        pass

    def destroy(self):
        """Drops collection of current repository.
                
        """
        pass
