import json
import httpx


class GraphResponseParser:
    """Simple helper class for grouping functionality and standardizing behaviours concerned with the unpacking and interpretating of
    the responses returned from the Graph API."""

    @staticmethod
    def response_parse(response: httpx.Response) -> dict:
        """Attempt to parse a httpx.Response instance, raising appropriate errors if the response is erroneous, or
        alternatively returning the data if the request was a success."""
        if response.is_success:
            return response.json()
        else:
            raise Exception(
                f"Query failed with status code {response.status_code}", response
            )
