import pymongo

from pymongo import MongoClient

#First get connected to the Mongodb
connection = MongoClient('localhost',27017)

#Once connection is successfull get the db instance
db= connection.sunil

#From the db get the collections
names= db.sunilCollections

#Find the item and print the corresponding one
item = names.find_one()
print(item['address']) 