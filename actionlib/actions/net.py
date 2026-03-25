"""Net actions - HTTP requests."""

from actionlib.core.registry import registry


def _http_get(url: str) -> str:
    """Perform HTTP GET request."""
    import urllib.request
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


def _http_post(url: str, data: str = "") -> str:
    """Perform HTTP POST request."""
    import urllib.request
    import urllib.parse
    data_bytes = urllib.parse.urlencode({"data": data}).encode("utf-8")
    with urllib.request.urlopen(url, data=data_bytes) as response:
        return response.read().decode("utf-8")


# Register net actions
registry.register("http_get", _http_get)
registry.register("http_post", _http_post)
