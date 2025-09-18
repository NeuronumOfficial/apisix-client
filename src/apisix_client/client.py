import httpx

from apisix_client.consumer.client import ApisixConsumerClient

APISIX_URL_DEFAULT = "http://localhost:9100"


class ApisixClient:
    def __init__(self, base_url: str | None, api_key: str, *args, **kwargs) -> None:
        self._base_url = (base_url or APISIX_URL_DEFAULT) + "apisix/admin"
        self._httpx_client = httpx.Client(base_url=self._base_url, headers={"X-API-KEY": api_key})
        self.consumers = ApisixConsumerClient(self._httpx_client)
