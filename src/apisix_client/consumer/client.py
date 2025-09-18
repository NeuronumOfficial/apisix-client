import httpx

from apisix_client.base_models import BaseResponse, converter
from apisix_client.common import pythonize_json_response
from apisix_client.consumer.models import Consumer, ConsumerResponse


class ApisixConsumerClient:
    def __init__(self, httpx_client: httpx.Client, *args, **kwargs) -> None:
        self._httpx_client: httpx.Client = httpx_client
        self.url_postfix = "/consumers"

    def create(self, new_customer: Consumer) -> bool:
        req_body = converter.unstructure(new_customer)
        response = self._httpx_client.put(self.url_postfix, json=req_body)

        if response.status_code == 400:  # Bad request
            raise RuntimeError(
                "Bad request. Some of the provided value has wrong"
                f" type or provided group_id doesn't exists {req_body}"
            )

        return response.status_code == 201  # Created

    def get(self, username: str) -> BaseResponse[ConsumerResponse] | None:
        r = self._httpx_client.get(self.url_postfix + "/" + username)
        json_response = r.json()

        if "message" in json_response:
            raise RuntimeError(json_response["message"])

        return converter.structure(pythonize_json_response(json_response), BaseResponse[ConsumerResponse])

    def get_all(self):
        r = self._httpx_client.get(self.url_postfix)
        json_response = r.json()
        print(json_response)

        return tuple(
            converter.structure(pythonize_json_response(i), BaseResponse[ConsumerResponse])
            for i in json_response["list"]
        )

    def delete(self, username: str):
        r = self._httpx_client.delete(self.url_postfix + "/" + username)
        json_response = r.json()
        if "message" in json_response:
            raise RuntimeError(json_response["message"])

        if "deleted" in json_response:
            return int(json_response["deleted"])

    def count(self) -> int:
        r = self._httpx_client.get(self.url_postfix)
        json_response = r.json()

        return json_response["total"]
