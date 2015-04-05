from contextlib import closing
from flask import Flask, render_template

import random
import sqlite3
import requests

import settings

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(settings.DATABASE)


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/')
@app.route('/index')
@app.route('/mustache')
def index():

    api_url = 'https://api.instagram.com/v1/tags/mustache/media/recent?client_id={}'.format(settings.CLIENT_ID)

    data = requests.get(api_url).json()['data']

    thing1 = random.choice(data)
    thing2 = random.choice(data)

    one = thing1['images']['low_resolution']['url']
    two = thing2['images']['low_resolution']['url']

    return render_template('index.html', one=one, two=two)


@app.route('/geostaching')
def geostaching():

    api_url = 'https://api.instagram.com/v1/tags/geostaching/media/recent?client_id={}'.format(settings.CLIENT_ID)

    data = requests.get(api_url).json()['data']

    thing1 = random.choice(data)
    thing2 = random.choice(data)

    one = thing1['images']['low_resolution']['url']
    two = thing2['images']['low_resolution']['url']

    return render_template('index.html', one=one, two=two)


@app.route('/cats')
def cats():

    api_url = 'https://api.instagram.com/v1/tags/cats/media/recent?client_id={}'.format(settings.CLIENT_ID)

    data = requests.get(api_url).json()['data']

    thing1 = random.choice(data)
    thing2 = random.choice(data)

    one = thing1['images']['low_resolution']['url']
    two = thing2['images']['low_resolution']['url']

    return render_template('index.html', one=one, two=two)


@app.route('/catvsmustache')
def catvsmustache():

    cat = 'https://api.instagram.com/v1/tags/cat/media/recent?client_id={}'.format(settings.CLIENT_ID)
    mustache = 'https://api.instagram.com/v1/tags/mustache/media/recent?client_id={}'.format(settings.CLIENT_ID)

    cat_data = requests.get(cat).json()['data']
    mustache_data = requests.get(mustache).json()['data']

    thing1 = random.choice(cat_data)
    thing2 = random.choice(mustache_data)

    catpic = thing1['images']['low_resolution']['url']
    stachepic = thing2['images']['low_resolution']['url']

    return render_template('index.html', one=catpic, two=stachepic)


if __name__ == '__main__':
    app.debug = True
    app.run()
