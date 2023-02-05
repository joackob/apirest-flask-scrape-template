from flask import Flask
from sys import argv
from scrape import scrape_news, scrape_news_by
from flask import request
from flask import abort

app = Flask(import_name=__name__)


@app.route('/')
def index():
    try:
        return scrape_news()
    except:
        abort(502)


@app.route('/filterby')
def filterby():
    try:
        query = request.args
        query = query.get('query')
        return scrape_news_by(query)
    except:
        abort(502)


if __name__ == '__main__':
    mode_dev = len(argv) == 2 and argv[1] == 'dev'
    app.run(debug=mode_dev)
