
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.secondChapter
sChapterCollection = db.secondChapterCollection


def find():

    print("find, reporting for duty")

    query = {'value': {'$gt' : 5}}

    try:
        cursor = sChapterCollection.find(query)

    except Exception as e:
        print ("Unexpected error:", type(e), e)
    sanity = 0
    count =0
    for doc in cursor:
        print(doc)
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



find_one()

