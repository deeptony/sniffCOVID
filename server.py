#performing relevant imports
from flask import Flask, render_template, request, abort, session, flash, redirect, jsonify
from flask_cors import CORS
#instantiating server
server = Flask("flask_server")
CORS(server)

#defining routes

#route for landing page
@server.route('/')
def render_index():
    return render_template('landing.html')

#route for receiving data package
#package has key1, key2, key3, key4
@server.route('/data', methods = ["POST"])
def store_data():
    body = request.data
    print(body)
    return body


#statement to initiate server
if __name__ == '__main__':
    server.run(debug = True)
