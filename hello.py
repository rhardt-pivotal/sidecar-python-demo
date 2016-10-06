"""
A first simple Cloud Foundry Flask app

Author: Ian Huston
License: See LICENSE.txt

"""
import flask
from flask import Flask
import os
import requests

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def hello_world():
    return 'Hello World! I am instance ' + str(os.getenv("CF_INSTANCE_INDEX", 0))

@app.route('/health')
def health():
    ret = {'status': 'UP'}
    return flask.jsonify(**ret)


@app.route('/javafortune')
def javafortune():
    return fortune('http://localhost:8087/fortunes/random')

@app.route('/rubyfortune')
def rubyfortune():
    return fortune('http://localhost:8087/ruby-demo/javafortune')


@app.route('/endoftheworld')
def endoftheworld():
    return fortune('http://localhost:8087/ruby-demo/endoftheworld')

@app.route('/nodefortune')
def nodefortune():
    return fortune('http://localhost:8087/node-demo/javafortune')


@app.route('/gofortune')
def gofortune():
    return fortune('http://localhost:8087/go-demo/javafortune')


@app.route('/dockerfortune')
def dockerfortune():
    return fortune('http://localhost:8087/docker-demo/javafortune')

def fortune(url):
    response = requests.get(url)
    return flask.jsonify(**response.json())


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
