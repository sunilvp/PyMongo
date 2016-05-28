import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db= connection.sunil
names= db.sunilCollections
item = names.find_one()
print(item['address']) 