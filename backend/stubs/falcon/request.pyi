class Request:
    def __init__(self, env: dict[str, str]) -> None: ...
    def get_param(self, name: str) -> str | None: ...