from app.interfaces import Scraper, Router
from dataclasses import dataclass


@dataclass
class App:
    scraper: Scraper
    router: Router

    def run(self, debugmode: bool = False) -> None:
        self.router.defineRoute(route='/', fun=self.getNews)
        self.router.defineRoute(route='/filterby', fun=self.getNewsByQuery)
        self.router.run(debugmode=debugmode)
        pass

    def getNews(self) -> list[str]:
        news = self.scraper.getNews()
        return news

    def getNewsByQuery(self, query: str) -> list[str]:
        titles = self.scraper.getNews()
        titles = [title for title in titles if query in title]
        return titles
