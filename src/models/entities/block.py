import models.entities.mongodb as model


class Model(model.Model):
    def _default_attributes(self):
        """Returns default values for initial model state (without identifier attribute).
        This method also defines schema for current model.
        :rtype: dict
        """
        pass
