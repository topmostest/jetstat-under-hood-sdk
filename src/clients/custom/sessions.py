import requests

import basement.temporary as temporary


class Session(temporary.TemporaryObject):
    def __init__(self):
        """        
        """
        pass

    @property
    def instance(self):
        """Returns wrapped session instance.
        :rtype: requests.Session
        """
        pass

    def rollback_temp(self):
        """Eliminates temporary object.
                
        """
        pass


class Params:
    def __init__(self, method, uri, route=None, do_auth=True, **kwargs):
        """Available `kwargs`:
            – headers: dict
            – params: dict
            - data: any
            - json: dict
            – cookies: dict
            – timeout: float
            – allow_redirects: bool
            – verify: bool
            – cert: str
        :type method: str
        :type uri: str
        :type route: dict
        :type do_auth: bool
        """
        pass

    @property
    def method(self):
        """Returns request method.
        :rtype: str
        """
        pass

    @property
    def uri(self):
        """Returns request uri.
        :rtype: str
        """
        pass

    @property
    def route(self):
        """Returns request route params.
        :rtype: dict
        """
        pass

    @property
    def do_auth(self):
        """Returns request authorization flag.
        :rtype: bool
        """
        pass

    @property
    def others(self):
        """Returns request other params.
        :rtype: dict
        """
        pass


class RequestLoop:
    def __init__(self, params, response, repeat, counter):
        """
        :type params: Params
        :type response: requests.Response
        :type repeat: () -> requests.Response
        :type counter: int
        """
        pass

    @property
    def params(self):
        """Returns raw request params.
        :rtype: requests.PreparedRequest
        """
        pass

    @property
    def response(self):
        """Returns response instance.
        :rtype: requests.Response
        """
        pass

    @property
    def repeat(self):
        """Returns function that can be called to repeat request.
        :rtype: () -> requests.Response
        """
        pass

    @property
    def counter(self):
        """Returns repeated requests counter.
        :rtype: int
        """
        pass
