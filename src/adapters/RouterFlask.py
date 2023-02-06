from dataclasses import dataclass
from typing import Callable
from app.interfaces import Router
from flask import Flask
from flask import request
from flask import abort


@dataclass
class RouterFlask(Router, Flask):
    def __init__(self) -> None:
        super().__init__(import_name=__name__)

    def run(self, debugmode: bool) -> None:
        Flask.run(self, debug=debugmode)

    def defineRouteIndex(self, action: Callable[[], list[str]]) -> None:
        self.add_url_rule(rule='/', view_func=action)

    def defineRouteFilter(self, action: Callable[[str], list[str]]) -> None:
        def filterByQuery():
            try:
                args = request.args()
                query = args.get('query')
                return action(query)
            except:
                abort(502)

        self.add_url_rule(rule='/filterby', view_func=filterByQuery)
