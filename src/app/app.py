from interfaces.interfaces import Scraper, Router
from dataclasses import dataclass


class App:
    def __init__(self, scraper: Scraper, router: Router) -> None:
        self.scraper = scraper
        self.router = router
        self.router.add_route_news(handler=self.get_news)

    def run(self) -> None:
        self.router.run()
        self.scraper.run()

    def get_news(self, key_words: str = '') -> list[str]:
        news = self.scraper.get_news()
        if key_words == '':
            return news
        news = [title for title in news if key_words in title]
        return news
