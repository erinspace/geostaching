from flask import Flask
app = Flask(__name__)

from flask import render_template

import requests
import random 

import settings

@app.route('/')
@app.route('/index')
@app.route('/mustaches')
def index():

    api_url = 'https://api.instagram.com/v1/tags/mustache/media/recent?client_id={}'.format(settings.CLIENT_ID)

    data = requests.get(api_url).json()['data']

    thing1 = random.choice(data)
    thing2 = random.choice(data)

    one = thing1['images']['low_resolution']['url']
    two = thing2['images']['low_resolution']['url']

    return render_template('index.html', one=one, two=two)

    # return '<html><img src={}><img src={}></html>'.format(one, two)


@app.route('/cats')
def cats():

    api_url = 'https://api.instagram.com/v1/tags/cats/media/recent?client_id={}'.format(settings.CLIENT_ID)

    data = requests.get(api_url).json()['data']

    thing1 = random.choice(data)
    thing2 = random.choice(data)

    one = thing1['images']['low_resolution']['url']
    two = thing2['images']['low_resolution']['url']

    return '<html><img src={}><img src={}></html>'.format(one, two)

if __name__ == '__main__':
    app.debug = True
    app.run()
