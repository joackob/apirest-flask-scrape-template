from sys import argv
from scraper import ScrapeNews
from router import RouterFlask
from app import App

app = App(scraper=ScrapeNews(), router=RouterFlask())
mode_dev = len(argv) == 2 and argv[1] == 'dev'
app.run(debugmode=mode_dev)
