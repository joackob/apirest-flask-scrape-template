from flask import Flask
from sys import argv
from scrape import scrape_clarin, scrape_infobae, scrape_clarin_with
from flask import request

app = Flask(import_name=__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route('/clarin')
def clarin():
    params = request.args
    if 'query' in params:
        return scrape_clarin_with(query=params.get('query'))
    else:
        return scrape_clarin()


@app.route('/infobae')
def infobae():
    return scrape_infobae()


if __name__ == '__main__':
    mode_dev = len(argv) == 2 and argv[1] == 'dev'
    app.run(debug=mode_dev)
