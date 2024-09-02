from typing import Any, Iterable
import falcon.app

class _ResultBase:
    def __init__(self, status: str, headers: dict[str, str]): ...
    @property
    def status(self) -> str: ...
    @property
    def headers(self) -> dict[str, str]: ...

class Result(_ResultBase):
    def __init__(self, iterable: Iterable[bytes], status: str, headers: dict[str, str]): ...
    @property
    def json(self) -> Any: ...

class TestClient: 
    def __init__(self, app: falcon.app.App): ...
    def simulate_get(self, path: str) -> Result: ...