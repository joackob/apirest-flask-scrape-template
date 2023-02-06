from sys import argv
from adapters.ScraperSoup import ScraperSoup
from adapters.RouterFlask import RouterFlask
from app.app import App

devmode = len(argv) == 2 and argv[1] == 'dev'
app = App(scraper=ScraperSoup(), router=RouterFlask())
app.run(debugmode=devmode)
