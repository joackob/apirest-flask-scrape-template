from requests import get
from bs4 import BeautifulSoup


class Soup(BeautifulSoup):
    def __init__(self, url: str):
        html = get(url=url)
        super().__init__(markup=html.text, features='html.parser')
        pass


def scrape_clarin() -> list[str]:
    url_clarin = 'https://www.clarin.com/'
    clarin_web = Soup(url_clarin)
    articulos = clarin_web.find_all(name='article')
    titulos = [articulo.find(name='h2') for articulo in articulos]
    titulos = [titulo.text for titulo in titulos]
    return titulos


def scrape_infobae() -> list[str]:
    url_infobae = 'https://www.infobae.com/'
    infobae_web = Soup(url_infobae)
    titulos = infobae_web.find_all(name='h2')
    titulos: list[str] = [titulo.text for titulo in titulos]
    titulos = [titulo for titulo in titulos if not titulo.isupper()]
    return titulos


def scrape_news() -> list[str]:
    return scrape_clarin() + scrape_infobae()


def scrape_news_by(words: str) -> list[str]:
    news = scrape_news()
    news = [title for title in news if words in title]
    return news
