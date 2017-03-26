from bottle import template,route,run
@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('hello {{name}},how are you?',name=name)
run(host='localhost',port=8080,debug=True)

