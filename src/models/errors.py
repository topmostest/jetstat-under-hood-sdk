import models.entities as entities


class ModelNotFoundError(Exception):
    def __init__(self, model, where):
        """
        :type model: type[entities.Model]
        :type where: any
        """
        pass

    @property
    def model(self):
        """Returns not found model class.
        :rtype: type[entities.Model]
        """
        pass

    @property
    def where(self):
        """Returns condition at which model unable to found
                
        """
        pass
