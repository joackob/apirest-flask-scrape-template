from scraper import ScrapeNews
from router import RouterFlask
from app import App

app = App(scraper=ScrapeNews(), router=RouterFlask())
app.run(debugmode=True)
