from dataclasses import dataclass
from typing import Callable
from interfaces.interfaces import Router
from flask import Flask
from flask import request
from flask import abort


@dataclass
class RouterFlask(Router, Flask):
    def __init__(self) -> None:
        Flask.__init__(self, import_name=__name__)

        def welcome_message():
            return 'Welcome to scrappe news'

        self.add_url_rule(rule='/', view_func=welcome_message)

    def run(self) -> None:
        Flask.run(self)

    def add_route_news(self, handler: Callable[[str], list[str]]) -> None:
        route = '/api/v1/news'

        def handler_route_news():
            try:
                words = request.args.get(key='words', default='')
                news = handler(words)
                return news
            except:
                abort(502)

        self.add_url_rule(rule=route, view_func=handler_route_news)
