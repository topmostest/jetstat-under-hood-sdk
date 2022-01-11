import models.entities.service as model


class Model(model.Model):
    def _default_attributes(self):
        """Returns default values for initial model state (without identifier attribute).
        This method also defines schema for current model.
        :rtype: dict
        """
        pass

    def refreshed_token(
        self,
        access_token,
        expiration=None,
        refresh_token=None,
        time_delta_unit='minutes'
    ):
        """Updates refreshed access token in all credentials.
        :type access_token: str
        :type expiration: int
        :type refresh_token: str
        :type time_delta_unit: str
        :rtype: int
        """
        pass
