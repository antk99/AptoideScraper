class App:
    def __init__(self, cors_enable: bool = False) -> None: ...
    def add_route(self, uri_template: str, resource: object) -> None: ...