from flask import Flask
from sys import argv

app = Flask(import_name=__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    mode_dev = len(argv) == 2 and argv[1] == 'dev'
    app.run(debug=mode_dev)
