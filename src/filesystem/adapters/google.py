import clients.google.auth as google_auth
import filesystem


class Adapter(filesystem.Adapter):
    def __init__(self, client):
        """
        :type client: google_auth.Client
        """
        pass

    @property
    def client(self):
        """Returns google client.
        :rtype: google_auth.Client
        """
        pass
