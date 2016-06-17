import pymongo
import sys
from pymongo.message import query
from pydoc import doc

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
students = db.students

def printInSortedWay():

    print("find, reporting for duty Find and Delete")
    query = {'type': 'homework'}

    try:
        cursor = students.find()
    except Exception as e:
        print ("Unexpected error:", type(e), e)
    
    for doc in cursor:
        score = doc["scores"]
        prevScore = 99999
        lowScore = "empty"
        for inScore in score:
            print(inScore)
            if inScore["type"] == "homework" and inScore["score"] < prevScore:
                prevScore = inScore["score"]
                lowScore = inScore   
                
        findQuery = {'_id': doc['_id']} 
        updateCommand = {'$pull' : {'scores' : { 'score' : prevScore}}}
        students.update(findQuery, updateCommand, upsert=False)
                
        print(lowScore)                 


printInSortedWay()