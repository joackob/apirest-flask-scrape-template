from requests import get
from bs4 import BeautifulSoup


def scrape_clarin() -> list[str]:
    url_clarin = 'https://www.clarin.com/'
    clarin_html = get(url=url_clarin)
    clarin_web = BeautifulSoup(markup=clarin_html.text, features='html.parser')
    articulos = clarin_web.find_all(name='article')
    titulos = [articulo.find(name='h2') for articulo in articulos]
    titulos = [titulo.text for titulo in titulos]
    return titulos


def scrape_clarin_with(query: str) -> list[str]:
    titulos = scrape_clarin()
    titulos = [titulo for titulo in titulos if query in titulo]
    return titulos


def scrape_infobae() -> list[str]:
    url_infobae = 'https://www.infobae.com/'
    infobae_html = get(url=url_infobae)
    infobae_web = BeautifulSoup(
        markup=infobae_html.text,
        features='html.parser')
    titulos = infobae_web.find_all(name='h2')
    titulos: list[str] = [titulo.text for titulo in titulos]
    titulos = [titulo for titulo in titulos if not titulo.isupper()]
    return titulos
