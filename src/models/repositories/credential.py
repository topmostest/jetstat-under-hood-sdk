import models
import models.repositories.mongodb as repository


class Repository(repository.Repository):
    @property
    def _model_ctor(self):
        """Returns covered model constructor.
        :rtype: type[models.Model]
        """
        pass

    @property
    def _collection_name(self):
        """Returns collection name.
        :rtype: str
        """
        pass
