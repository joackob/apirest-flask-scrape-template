from typing import Callable
from abc import abstractmethod


class Router:
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_route_news(self, handler: Callable[[str], list[str]]) -> None:
        raise NotImplementedError


class Scraper:
    @abstractmethod
    def get_news(self) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError
