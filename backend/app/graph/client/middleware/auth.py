import asyncio
from datetime import datetime, timedelta
import threading
from typing import Optional
import httpx
import msal


class GraphAuthMiddleware(httpx.Auth):
    def __init__(self, client_id: str, authority: str, secret: str, scope: str) -> None:

        self.__graph_app = msal.ConfidentialClientApplication(
            client_id=client_id, authority=authority, client_credential=secret
        )
        self._scope = scope

        self._sync_lock = None
        self._async_lock = None

    def __get_token(self) -> str:
        result = self.__graph_app.acquire_token_silent([self._scope], account=None)

        if not result:
            result = self.__graph_app.acquire_token_for_client(scopes=self._scope)

        if "access_token" in result:
            return result["access_token"]
        else:
            raise Exception("Could not acquire token", result)

    def sync_get_token(self):
        if not self._sync_lock:
            self._sync_lock = threading.RLock()

        with self._sync_lock:
            return self.__get_token()

    async def async_get_token(self):
        if not self._async_lock:
            self._async_lock = asyncio.Lock()

        async with self._async_lock:
            return self.__get_token()

    def sync_auth_flow(self, request):
        token = self.sync_get_token()
        request.headers["Authorization"] = f"Bearer {token}"
        yield request

    async def async_auth_flow(self, request):
        token = self.sync_get_token()
        request.headers["Authorization"] = f"Bearer {token}"
        yield request
