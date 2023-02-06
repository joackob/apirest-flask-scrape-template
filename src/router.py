from dataclasses import dataclass
from typing import Callable
from interfaces import Router
from flask import Flask


@dataclass
class RouterFlask(Router):
    router: Flask

    def __init__(self) -> None:
        super().__init__()
        self.router = Flask(__name__)

    def run(self, debugmode: bool) -> None:
        self.router.run(debug=debugmode)

    def defineRoute(self, route: str, fun: Callable[[], list[str]]) -> None:
        self.router.add_url_rule(rule=route, view_func=fun)
