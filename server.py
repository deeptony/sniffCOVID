#performing relevant imports
from flask import Flask, render_template, request, abort, session, flash, redirect, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from flask_heroku import Heroku

#instantiating server
server = Flask("flask_server")
CORS(server)
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(server)
db = SQLAlchemy(server)

#models can only be imported after the db has been instantiated
from models import Point

#defining routes
#route for landing page
@server.route('/')
def render_index():
    return render_template('landing.html')

#route for receiving data package
#package has key1, key2, key3, key4
@server.route('/data', methods = ["POST"])
def store_data():
    body = jsonify(request.data)
    print(body.key1)
    return body


#statement to initiate server
if __name__ == '__main__':
    server.run(debug = True)
