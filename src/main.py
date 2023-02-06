from sys import argv
from adapters.scraper import ScrapeNews
from adapters.router import RouterFlask
from app.app import App

devmode = len(argv) == 2 and argv[1] == 'dev'
app = App(scraper=ScrapeNews(), router=RouterFlask())
app.run(debugmode=devmode)
