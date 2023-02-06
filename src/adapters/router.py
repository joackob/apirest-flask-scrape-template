from dataclasses import dataclass
from typing import Callable
from app.interfaces import Router
from flask import Flask


@dataclass
class RouterFlask(Router, Flask):
    def __init__(self) -> None:
        super().__init__(import_name=__name__)

    def run(self, debugmode: bool) -> None:
        Flask.run(self, debug=debugmode)

    def defineRoute(self, route: str, fun: Callable[[], list[str]]) -> None:
        self.add_url_rule(rule=route, view_func=fun)
