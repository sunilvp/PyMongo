
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.secondChapter
sChapterCollection = db.secondChapterCollection


def find():

    print("find, reporting for duty command test")

    query = {'value': {'$gt' : 5}}
    projection = {'insert' : 1, 'name':1, '_id': 0}

    try:
        cursor = sChapterCollection.find(query, projection)

    except Exception as e:
        print ("Unexpected error:", type(e), e)
    sanity = 0
    count =0
    for doc in cursor:
        print(doc)
        print(doc['insert'],"sunil")
        sanity += 1
        count +=1
        if (sanity > 10):
            break
        
    print("Count is ", count)
        


def find_one():

    print("find one, reporting for duty")
    query = {'value':10}
    
    try:
        doc = sChapterCollection.find_one(query)
        
    except Exception as e:
        print("Unexpected error:", type(e), e)

    
    print( doc)



find()

