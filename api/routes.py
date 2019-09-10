from flask import current_app, Blueprint, jsonify
import requests


api = Blueprint('api', __name__)
URL = 'https://api.github.com'


@api.route('/')
def index():
    return "hello world"

@api.route('/repo/<reponame>')
def repo(reponame):
    r = requests.get(URL + '/repos/0054/' + reponame).json()
    return r

@api.route('/check')
def events():
    r = requests.get(URL).json()
    return r
