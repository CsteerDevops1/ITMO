#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/hello/<string:name>')
def hello(name):
    return f'Hello, {name}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
