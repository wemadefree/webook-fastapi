from dataclasses import dataclass
from typing import Generator, Optional, Union

import httpx
import msal
from app.graph.client.middleware.auth import GraphAuthMiddleware
from app.graph.client.middleware.transport import RetryTransport
from app.graph.client.response_parser import GraphResponseParser


@dataclass
class GraphClient:
    graph_base_url: str = "https://graph.microsoft.com/v1.0/"

    httpx_client: Optional[httpx.Client] = None

    client_id: Optional[str] = None
    authority: Optional[str] = None
    client_credential: Optional[str] = None
    scope: Optional[str] = "https://graph.microsoft.com/.default"

    def exhaust(self, response_or_url: Union[httpx.Response, str]) -> Generator:
        next_link: Optional[str] = None
        if isinstance(response_or_url, str):
            next_link = response_or_url

        while True:
            if next_link:
                response = self.httpx_client.get(next_link)

            data: dict = response.json()

            if "value" not in data:
                break

            for item in data["value"]:
                yield item

            if not data.get("@odata.nextLink"):
                break

            next_link = data["@odata.nextLink"]

    def __resource_fab(self, type):
        return type(self)

    def _url_build(self, postfix):
        return self.graph_base_url + postfix

    def __post_init__(self):
        self.httpx_client = httpx.Client(
            auth=GraphAuthMiddleware(
                client_id=self.client_id,
                authority=self.authority,
                secret=self.client_credential,
                scope=self.scope,
            ),
            transport=RetryTransport(),
        )

        self.users: UserResource = self.__resource_fab(UserResource)
        self.groups: GroupResource = self.__resource_fab(GroupResource)


@dataclass
class BaseGraphResource:
    graph_client: Optional[GraphClient] = None
    resource_fragment: Optional[str] = None

    @property
    def _gq(self):
        """Shorthand for self.graph_client.httpx_client
        'gq' abbreviates Graph Query
        """
        return self.graph_client.httpx_client

    def get_all(self):
        return self.graph_client.list(
            self._gq.get(url=self._endpoint_url + "?$top=999")
        )

    def get(self, id):
        return GraphResponseParser.strict_parse(
            self._gq.get(url=self._endpoint_url + "/" + str(id))
        )

    def __post_init__(self):
        self._endpoint_url = self.graph_client._url_build(self.resource_fragment)


@dataclass
class GroupResource(BaseGraphResource):
    resource_fragment: Optional[str] = "groups"

    def get_group_members(self, group_id: str):
        return self.graph_client.list(
            self._gq.get(url=self._endpoint_url + "/" + str(group_id) + "/members")
        )


@dataclass
class UserResource(BaseGraphResource):
    resource_fragment: Optional[str] = "users"
