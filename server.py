#performing relevant imports
from flask import Flask, render_template, request, abort, session, flash, redirect

#instantiating server
server = Flask("flask_server")

#defining routes

#route for landing page
@server.route('/')
def render_index():
    return render_template('landing.html')


#statement to initiate server
if __name__ == '__main__':
    server.run(debug = True)
