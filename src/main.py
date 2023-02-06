from sys import argv
from scraper import ScrapeNews
from router import RouterFlask
from app import App

mode_dev = len(argv) == 2 and argv[1] == 'dev'
app = App(scraper=ScrapeNews(), router=RouterFlask())
app.run(debugmode=mode_dev)
