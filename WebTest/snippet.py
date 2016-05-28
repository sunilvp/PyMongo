from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello user {{name}}</b>!', name=name)

run(host='localhost', port=8080)