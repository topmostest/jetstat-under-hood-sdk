import abc

import bson

import models.entities.model as model


class Model(model.Model):
    def _defaults(self):
        """Returns default values for initial model state.
        This method also defines schema for current model.
        :rtype: dict
        """
        pass

    @abc.abstractmethod
    def _default_attributes(self):
        """Returns default values for initial model state (without identifier attribute).
        This method also defines schema for current model.
        :rtype: dict
        """
        raise NotImplementedError()

    def get_id_attribute(self):
        """Getter of `id`.
        :rtype: str
        """
        pass

    def set_id_attribute(self, value):
        """Setter of `id`.
        :type value: str|bson.ObjectId
        """
        pass
