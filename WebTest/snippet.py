from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello user {{name}}</b>!', name=name)

#Using Bottle python module to start a webserver and route a simple url example
run(host='localhost', port=8080)