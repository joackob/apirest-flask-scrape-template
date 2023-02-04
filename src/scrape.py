from requests import get
from bs4 import BeautifulSoup


def scrape_clarin() -> list[str]:
    url_clarin = 'https://www.clarin.com/'
    clarin_html = get(url=url_clarin)
    clarin_web = BeautifulSoup(markup=clarin_html.text, features='html.parser')
    articulos = clarin_web.find_all(name='article')
    titulos = [articulo.find('h2') for articulo in articulos]
    titulos = [titulo.text for titulo in titulos]
    return titulos
