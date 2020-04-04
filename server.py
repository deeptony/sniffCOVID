#performing relevant imports
from flask import Flask, render_template, request, abort, session, flash, redirect

#instantiating server
server = Flask("flask_server")

#defining routes

#route for landing page
@server.route('/')
def render_index():
    return render_template('landing.html')

#route for input form
@server.route('/input')
def render_form():
    return render_template('input.html')
    
#statement to initiate server
if __name__ == '__main__':
    server.run(debug = True)
