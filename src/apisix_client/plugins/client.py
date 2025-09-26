from typing import Tuple

import httpx


class PluginClient:
    def __init__(self, httpx_client: httpx.Client, *args, **kwargs) -> None:
        self._httpx_client: httpx.Client = httpx_client
        self.url_postfix = "/plugins"

    def get_available(self) -> Tuple[str, ...]:
        response = self._httpx_client.get(self.url_postfix + "/list")
        return tuple(response.json())

    def reload(self) -> bool:
        response = self._httpx_client.put(self.url_postfix + "/reload")
        return response.text == "done"
