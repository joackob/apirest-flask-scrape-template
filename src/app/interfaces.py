from collections.abc import Callable
from abc import abstractmethod


class Router:
    @abstractmethod
    def run(self, debugmode: bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def defineRouteIndex(self, action: Callable[[], list[str]]) -> None:
        raise NotImplementedError

    @abstractmethod
    def defineRouteFilter(self, action: Callable[[str], list[str]]) -> None:
        raise NotImplementedError


class Scraper:
    @abstractmethod
    def getNews(self) -> list[str]:
        raise NotImplementedError
