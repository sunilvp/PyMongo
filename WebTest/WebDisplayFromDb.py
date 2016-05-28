#Sample end to end program which uses bottle for the webserver and pymongo for db interaction
import bottle
import pymongo

from bottle import route, run, template
from pymongo import MongoClient

@route('/hello/')
def index():
    connection = MongoClient('localhost',27017)
    db= connection.sunil
    names= db.sunilCollection
    item = names.find_one()
    return '<b>Hello user %s</b>!' %item["name"]
#%s specifies an argument which has to be printed.
run(host='localhost', port=8080)