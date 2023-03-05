from requests import get
from bs4 import BeautifulSoup
from interfaces.interfaces import Scraper


class Soup(BeautifulSoup):
    def __init__(self, url: str):
        html = get(url=url)
        super().__init__(markup=html.text, features='html.parser')
        pass


class ScraperSoup(Scraper):
    def run(self) -> None:
        pass

    def get_news(self) -> list[str]:
        return self.scrape_clarin() + self.scrape_infobae()

    def scrape_clarin(self) -> list[str]:
        url_clarin = 'https://www.clarin.com/'
        clarin_web = Soup(url_clarin)
        articulos = clarin_web.find_all(name='article')
        titulos = [articulo.find(name='h2') for articulo in articulos]
        titulos = [titulo.text for titulo in titulos]
        return titulos

    def scrape_infobae(self) -> list[str]:
        url_infobae = 'https://www.infobae.com/'
        infobae_web = Soup(url_infobae)
        titulos = infobae_web.find_all(name='h2')
        titulos: list[str] = [titulo.text for titulo in titulos]
        titulos = [titulo for titulo in titulos if not titulo.isupper()]
        return titulos
