import logging

import httpx

from apisix_client.consumer.client import ConsumerClient
from apisix_client.plugins.client import PluginClient
from apisix_client.protocols import Logger
from apisix_client.route.client import RouteClient

APISIX_URL_DEFAULT = "http://localhost:9100"

LOGGER = logging.getLogger(__name__)


class ApisixClient:
    def __init__(
        self, base_url: str | None, api_key: str, logger: Logger | None = None, *args, **kwargs
    ) -> None:
        self._base_url = (base_url or APISIX_URL_DEFAULT) + "apisix/admin"
        self._httpx_client = httpx.Client(base_url=self._base_url, headers={"X-API-KEY": api_key})
        self._logger: Logger = LOGGER if logger is None else logger

        self.consumers = ConsumerClient(self._httpx_client, logger=self._logger)
        self.plugins = PluginClient(self._httpx_client, logger=self._logger)
        self.route = RouteClient(self._httpx_client, logger=self._logger)
