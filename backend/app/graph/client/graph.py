from dataclasses import dataclass
from typing import Generator, Optional

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

    def list(self, response: httpx.Response) -> Generator:
        """Helper method generator intended to aid in reading a list of data from the Graph API.
        Takes an initial response, and continues chasing nextLinks until Graph API has been exhausted.
        You might want to set the ?$top query variable depending on your use case -- by default we get 100 per request/page, and the maximum is 999.
        This $top query variable (and all other variables in the OG request for that matter) will be carried into the subsequent paginated queries/requests.
        """

        response = response
        params = {}

        while True:
            if "@odata.nextLink" in params:
                response = self.httpx_client.get(params["@odata.nextLink"])

            response_values = GraphResponseParser.response_parse(response)

            if not response_values["value"]:
                break

            for item in response_values["value"]:
                yield item

            if not response_values.get("@odata.nextLink"):
                break

            params["@odata.nextLink"] = response_values.get("@odata.nextLink")

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
