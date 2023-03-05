from sys import argv
from scrapper.ScraperSoup import ScraperSoup
from router.RouterFlask import RouterFlask
from app.app import App


def main():
    app = App(scraper=ScraperSoup(), router=RouterFlask())
    app.run()


if __name__ == '__main__':
    main()
