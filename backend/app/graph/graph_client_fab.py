from typing import List

from app.core.config import GRAPH_AUTHORITY, GRAPH_CLIENT_ID, GRAPH_CLIENT_SECRET
from app.graph.client.graph import GraphClient


def create_graph_client() -> None:
    print(GRAPH_CLIENT_ID)
    print(GRAPH_CLIENT_SECRET)
    print(GRAPH_AUTHORITY)

    if not all([GRAPH_CLIENT_ID, GRAPH_CLIENT_SECRET, GRAPH_AUTHORITY]):
        return None

    graph_api_client = GraphClient(
        client_id=GRAPH_CLIENT_ID,
        authority=GRAPH_AUTHORITY,
        client_credential=GRAPH_CLIENT_SECRET,
    )

    return graph_api_client
