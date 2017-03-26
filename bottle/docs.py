# hello world
from bottle import route, run
@route('/hello')
def hello():
    return 'Hello World!'
run(host='localhost',port=8080,debug=True)

# create an app
from bottle import Bottle, run
app = Bottle()
@app.route('/hello')
def hello():
    return 'Hello World!'
run(app,host='localhost',port=8080)

# bind more than one route to a single callback
from bottle import template,route,run
@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('hello {{name}},how are you?',name=name)
run(host='localhost',port=8080,debug=True)

# filters
# usage: @route('/<name:filter:config>') or @route('/<name:filter>)'
# type: int float path re

# routing static files
# use mimetype to disable guessing
from bottle import static_file
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename,root='/path/to/your/static/files')
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath,root='/path/to/your/static/files')

# errors pages
from bottle import error
@error(404)
def error404(error):
    return 'Nothong here,sorry'

# rasie errors
from bottle import route, abort
@route('/restricted')
def restricted():
    abort(401,'Sorry, access denied')

# redirect
from bottle import dedirect
@route('/wrong/url')
def wrong():
    redirect('/right/url')

# response header
response.set_header('key','value')
response.add_header('key','value')
# cookie
request.get_cookie('key')
response.set_cookie('key','value')
