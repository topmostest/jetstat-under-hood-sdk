import models.entities.mongodb as model


class Model(model.Model):
    def _default_attributes(self):
        """Returns default values for initial model state (without identifier attribute).
        This method also defines schema for current model.
        :rtype: dict
        """
        pass

    def get_id_attribute(self):
        """Getter of `id`.
                
        """
        pass

    def set_id_attribute(self, value):
        """Setter of `id`.
        :type value: any
        """
        pass

    def get_db_id_attribute(self):
        """Getter of `db_id`.
        :rtype: str
        """
        pass

    def set_db_id_attribute(self, value):
        """Setter of `db_id`.
        :type value: str|bson.ObjectId
        """
        pass
