import abc

import requests

import clients.custom.sessions as sessions
import models


class Client:
    def __init__(self, credential=None, locale=None):
        """
        :type credential: models.Credential
        :type locale: str
        """
        pass

    @property
    @abc.abstractmethod
    def _defaults(self):
        """Returns default parameters such as:
            – base_uri: str
            - encoding: str (defaults to UTF-8)
            – headers: dict
            – params: dict
            – cookies: dict
            – timeout: float
            – allow_redirects: bool
            – verify: bool
            – cert: str
        :rtype: dict
        """
        raise NotImplementedError()

    @property
    def _status_hooks(self):
        """Returns status hook map.
        Key is name of event.
        Value is function which checks status for belonging to its key.
        :rtype: dict[str, (int) -> bool]
        """
        pass

    @property
    def _proxy_mode(self):
        """Returns proxy mode.
        * Positive value – select host before each request;
        * Zero value – select host once during session initialization;
        * Negative value – don't use proxy.
        :rtype: int
        """
        pass

    @property
    def _raising_events(self):
        """Returns true if request events are raising.
        :rtype: bool
        """
        pass

    def _prepare_url(self, base, uri, route):
        """Prepares full url for future request.
        :type base: str
        :type uri: str
        :type route: dict
        :rtype: str
        """
        pass

    def _merge_defaults(self, default, override):
        """Default way to merge override data with default one.
        :type default: any
        :type override: any
        """
        pass

    def _merge_defaults_dicts(self, default, override):
        """Merges dict-based override data with default one.
        :type default: dict
        :type override: dict
        :rtype: dict
        """
        pass

    def _merge_default_headers(self, default, override):
        """Merges override headers with default ones.
        :type default: dict
        :type override: dict
        :rtype: dict
        """
        pass

    def _merge_default_params(self, default, override):
        """Merges override GET-params with default ones.
        :type default: dict
        :type override: dict
        :rtype: dict
        """
        pass

    def _make_request(self, method, uri, route=None, **kwargs):
        """Returns request instance to be sent.
        Available `kwargs`:
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
        :rtype: requests.Request
        """
        pass

    def _prepare_authorization(self, request, credential):
        """Prepares request to be authorized
        :type request: requests.Request
        :type credential: models.Credential
        """
        pass

    @abc.abstractmethod
    def _refresh_authorization(self, credential):
        """Performs refreshing of credential's access token.
        Returns kv-params for `credential.refreshed_token` method.
        :type credential: models.Credential
        :rtype: dict
        """
        raise NotImplementedError()

    def _send_via_session(self, request):
        """Sends request -> returns response.
        :type request: requests.PreparedRequest
        :rtype: requests.Response
        """
        pass

    def _request(self, method, uri, route=None, do_auth=True, **kwargs):
        """Sends request -> returns response.
        Available `kwargs`:
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
        :rtype: requests.Response
        """
        pass

    def _rec_request(self, params, counter):
        """Recursive version of `_request` method.
        :type params: sessions.Params
        :type counter: int
        :rtype: requests.Response
        """
        pass

    def _process_response(self, params, response, counter, event_info):
        """Handles response before return it.
        :type params: sessions.Params
        :type response: requests.Response
        :type counter: int
        :type event_info: tuple
        :rtype: requests.Response
        """
        pass

    def _handle_bad_connection(self, loop):
        """Handles `bad_connection` status.
        :type loop: sessions.RequestLoop
        :rtype: requests.Response
        """
        pass

    def _handle_refresh_token(self, loop):
        """Handles `refresh_token` status.
        :type loop: sessions.RequestLoop
        :rtype: requests.Response
        """
        pass

    def _handle_client_error(self, loop):
        """Handles `client_error` status.
        :type loop: sessions.RequestLoop
        :rtype: requests.Response
        """
        pass

    def _handle_server_error(self, loop):
        """Handles `server_error` status.
        :type loop: sessions.RequestLoop
        :rtype: requests.Response
        """
        pass

    def _handle_ok(self, loop):
        """Handles `ok` status.
        :type loop: sessions.RequestLoop
        :rtype: requests.Response
        """
        pass


class JsonResponseBased:
    @property
    def _json_response_root(self):
        """Returns root key for json response.
        :rtype: str
        """
        pass

    def _json_response(self, response, root=None, default=None, whole=False, resp_encoding=None):
        """Returns response from json data.
        :type response: requests.Response
        :type root: str
        :type default: any
        :type whole: bool
        :type resp_encoding: str
        :rtype: dict
        """
        pass


class PaginatedResponses:
    @abc.abstractmethod
    def _continue_pagination(self, page, response):
        """Returns true if pagination is needed to be continued.
        :type page: int
        :type response: any
        :rtype: bool
        """
        raise NotImplementedError()

    def _paginate(self, request, start_page=0, page_limit=None):
        """Performs looped requests through all pages.
        :type request: (int) -> any
        :type start_page: int
        :type page_limit: int
        :rtype: typing.Generator
        """
        pass
